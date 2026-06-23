#!/usr/bin/env python3
"""
SEO/GEO knowledge-base scraper (same method as the klaviyo-marketing skill).

Discovers article URLs from each source's sitemap (explicit sitemap URLs with
recursive sitemap-index expansion, or trafilatura auto-discovery), extracts main
content with trafilatura (requests fallback for bot-hostile hosts), and writes one
markdown file per page (with frontmatter) into references/<source>/.

Then build the semantic index with index_kb.py (reuses the klaviyo-marketing
.venv: BGE-M3 -> LanceDB), and query with search.py.

Crawl policy: personal local learning KB only. Low frequency, source_url kept
for attribution, English-only, per-source caps. robots.txt allowance was verified
per source. Sources flagged tos_ok=False (commercial-ToS gray area) are included
per the user's explicit instruction but kept rate-limited & attributed.

Usage:
    python scrape_seo_geo.py --list
    python scrape_seo_geo.py --sources google-search-central schema-org
    python scrape_seo_geo.py --all
    python scrape_seo_geo.py --sources ahrefs-blog --limit 5   # test run
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlsplit

try:
    import requests
    import trafilatura
    from trafilatura.sitemaps import sitemap_search
except ImportError as e:  # pragma: no cover
    sys.exit(f"Missing dependency ({e}); run: pip install requests trafilatura")

SKILL_DIR = Path(__file__).resolve().parent
REF_DIR = SKILL_DIR / "references"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; seo-geo-kb/1.0; personal learning use)"}
SLEEP = 0.6
TIMEOUT = 30
DEFAULT_LIMIT = 400          # per-source cap for the huge blogs (0 = no cap)

# Per-source config.
#   sitemaps   : explicit sitemap/sitemap-index URLs (recursively expanded)
#   homepage   : fallback for trafilatura sitemap auto-discovery
#   include    : keep only URLs whose string contains ANY of these substrings
#   note       : stored in frontmatter `section`
#   tos_ok     : True = open/official; False = commercial ToS gray area
#   limit      : override DEFAULT_LIMIT (None = default; 0 = unlimited)
#   single_urls: explicit extra pages (bypass sitemap)
SOURCES: dict[str, dict] = {
    # ---- Tier 1: authoritative primary sources (open / official) ----
    "google-search-central": {
        "sitemaps": ["https://developers.google.com/sitemap.xml"],
        "homepage": "https://developers.google.com/search/docs",
        "include": [
            "/search/docs/appearance", "/search/docs/fundamentals",
            "/search/docs/crawling-indexing", "/search/docs/essentials",
            "/search/docs/monitor-debug", "/search/blog",
        ],
        "note": "Google Search Central — official technical SEO + structured data docs",
        "tos_ok": True,
        "limit": 0,
    },
    "schema-org": {
        "sitemaps": ["https://schema.org/docs/sitemap.xml"],
        "homepage": "https://schema.org/docs/schemas.html",
        "include": ["schema.org"],
        "note": "schema.org — structured-data vocabulary reference",
        "tos_ok": True,
        "limit": 0,
    },
    "geo-paper": {
        "include": [],
        "note": "Princeton GEO paper — Generative Engine Optimization (academic foundation)",
        "tos_ok": True,
        "single_urls": [
            "https://arxiv.org/abs/2311.09735",
            "https://arxiv.org/html/2311.09735v3",
        ],
    },
    # ---- Tier 2: SEO academies (robots.txt-permitted; commercial ToS gray area) ----
    "ahrefs-blog": {
        "sitemaps": ["https://ahrefs.com/blog/sitemap_index.xml"],
        "include": ["/blog/"],
        "note": "Ahrefs blog — SEO methodology",
        "tos_ok": False,
    },
    "ahrefs-academy": {
        "sitemaps": ["https://ahrefs.com/academy/sitemap.xml"],
        "include": ["/academy/"],
        "note": "Ahrefs Academy — SEO courses",
        "tos_ok": False,
        "limit": 0,
    },
    "semrush-blog": {
        "sitemaps": ["https://www.semrush.com/blog/sitemap/"],
        "include": ["/blog/"],
        "note": "Semrush blog — SEO/GEO methodology",
        "tos_ok": False,
    },
    # ---- Tier 3: GEO/AEO playbooks + SEO news ----
    "search-engine-journal": {
        "sitemaps": ["https://www.searchenginejournal.com/sitemap_index.xml"],
        "homepage": "https://www.searchenginejournal.com/",
        "include": ["/"],
        "note": "Search Engine Journal — SEO/GEO news + guides",
        "tos_ok": True,
    },
    "scrunch": {
        "homepage": "https://scrunch.com/blog",
        "include": ["/blog"],
        "note": "Scrunch — AEO/GEO playbook",
        "tos_ok": True,
        "limit": 0,
    },
    "daydream": {
        "homepage": "https://www.withdaydream.com/library",
        "include": ["/library"],
        "note": "Daydream — GEO library (how LLMs crawl & index)",
        "tos_ok": True,
        "limit": 0,
    },
}

LOCALE_RE = re.compile(r"^[a-z]{2}-[a-z]{2}$")


def slugify(text: str, maxlen: int = 90) -> str:
    text = re.sub(r"<[^>]+>", "", text or "").lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")[:maxlen] or "untitled"


def url_to_filename(url: str) -> str:
    parts = [p for p in urlsplit(url).path.split("/") if p]
    if parts and LOCALE_RE.match(parts[0]):
        parts = parts[1:]
    if parts and parts[0] in ("blog", "seo", "search", "docs", "library", "academy"):
        parts = parts[1:] or ["index"]
    return f"{slugify('-'.join(parts) or 'index')}.md"


def _fetch_text(url: str) -> str | None:
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
        return r.text
    except Exception as e:  # noqa: BLE001
        print(f"   ! fetch {url}: {e}", flush=True)
        return None


def expand_sitemaps(sitemap_urls: list[str], depth: int = 0) -> list[str]:
    """Recursively expand sitemap-index files into page URLs."""
    pages: list[str] = []
    for sm in sitemap_urls:
        txt = _fetch_text(sm)
        if not txt:
            continue
        locs = re.findall(r"<loc>\s*(.*?)\s*</loc>", txt)
        nested = [l for l in locs if l.lower().endswith(".xml") or l.rstrip("/").endswith("sitemap")]
        leaf = [l for l in locs if l not in nested]
        pages += leaf
        if nested and depth < 3:
            pages += expand_sitemaps(nested, depth + 1)
    return pages


def discover_urls(src_key: str, cfg: dict, limit: int) -> list[str]:
    urls: list[str] = list(cfg.get("single_urls", []))
    raw: list[str] = []
    if cfg.get("sitemaps"):
        raw = expand_sitemaps(cfg["sitemaps"])
    if not raw and cfg.get("homepage"):
        try:
            raw = sitemap_search(cfg["homepage"], target_lang="en")
        except Exception as e:  # noqa: BLE001
            print(f"   ! sitemap discovery failed for {src_key}: {e}", flush=True)
    inc = cfg.get("include") or [""]
    for u in raw:
        if "?" in u:                      # drop localized ?hl= / query variants
            continue
        parts = [p for p in urlsplit(u).path.split("/") if p]
        if parts and LOCALE_RE.match(parts[0]) and parts[0] != "en-us":
            continue
        if any(tok in u for tok in inc):
            urls.append(u)
    seen: set[str] = set()
    out = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    if limit:
        out = out[:limit]
    return out


def scrape_url(url: str, folder: str, note: str) -> bool:
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:                      # bot-hostile host -> requests fallback
        downloaded = _fetch_text(url)
    if not downloaded:
        return False
    body = trafilatura.extract(
        downloaded,
        output_format="markdown",
        include_links=True,
        include_tables=True,
        favor_recall=True,
    )
    if not body or len(body.strip()) < 120:
        return False
    meta = trafilatura.extract_metadata(downloaded)
    title = (getattr(meta, "title", None) or url.rstrip("/").split("/")[-1]).strip()
    date = getattr(meta, "date", None) or ""
    fm = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"source_url: {url}",
        f"category: {folder}",
        f"section: {json.dumps(note, ensure_ascii=False)}",
        f"date: {date}",
        "---",
        "",
        f"# {title}",
        "",
        body.strip(),
        "",
    ]
    out_dir = REF_DIR / folder
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / url_to_filename(url)).write_text("\n".join(fm), encoding="utf-8")
    return True


def main() -> None:
    ap = argparse.ArgumentParser(description="Scrape SEO/GEO sources into a local RAG KB.")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--sources", nargs="+")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    if args.list:
        print("Configured SEO/GEO sources:\n")
        for k, c in SOURCES.items():
            tos = "open" if c.get("tos_ok") else "GRAY"
            print(f"  [{tos:4s}] {k:22s} {c['note']}")
        print("\n[open] = official/permissive | [GRAY] = robots-permitted, commercial ToS")
        return

    keys = list(SOURCES) if args.all else (args.sources or [])
    if not keys:
        sys.exit("Specify --sources <keys> or --all (see --list).")
    bad = [k for k in keys if k not in SOURCES]
    if bad:
        sys.exit(f"Unknown sources: {bad}. Known: {list(SOURCES)}")

    grand_ok = grand_fail = 0
    for key in keys:
        cfg = SOURCES[key]
        limit = args.limit if args.limit is not None else cfg.get("limit", DEFAULT_LIMIT)
        if limit is None:
            limit = DEFAULT_LIMIT
        print(f"\n== {key}  (limit={limit or 'inf'}) -> references/{key}/", flush=True)
        urls = discover_urls(key, cfg, limit)
        print(f"   discovered {len(urls)} URLs", flush=True)
        ok = fail = skipped = 0
        for i, u in enumerate(urls, 1):
            out_path = REF_DIR / key / url_to_filename(u)
            if not args.force and out_path.exists():
                skipped += 1
                continue
            try:
                if scrape_url(u, key, cfg["note"]):
                    ok += 1
                else:
                    fail += 1
            except Exception as e:  # noqa: BLE001
                fail += 1
                print(f"   ! {u}: {e}", flush=True)
            if i % 25 == 0:
                print(f"   ... {i}/{len(urls)} (ok={ok} fail={fail} skip={skipped})", flush=True)
            time.sleep(SLEEP)
        print(f"  done: {ok} ok, {fail} failed/empty, {skipped} already-existed", flush=True)
        grand_ok += ok
        grand_fail += fail

    print(f"\nTotal: {grand_ok} written, {grand_fail} failed -> {REF_DIR}")
    print("Next: build the semantic index with index_kb.py (klaviyo .venv).")


if __name__ == "__main__":
    main()
