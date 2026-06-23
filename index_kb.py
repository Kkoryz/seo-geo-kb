#!/usr/bin/env python3
"""
Build a local semantic-search index over the SEO/GEO knowledge base.

Same pipeline as the klaviyo-marketing skill:
  - chunk each references/**/*.md by markdown headers (header-aware)
  - embed chunks with BGE-M3 (multilingual: 中文 queries match English docs)
  - store vectors + metadata in LanceDB (single-folder embedded vector store)

Run with the klaviyo-marketing .venv (already has torch + sentence-transformers
+ lancedb, and BGE-M3 is cached), pointed at THIS script:

    ~/.codex/skills/klaviyo-marketing/.venv/Scripts/python.exe \
      ~/.codex/skills/seo-geo-kb/index_kb.py
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


def _harden_windows_dll_path() -> None:
    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    if sys.platform != "win32":
        return
    venv = os.path.dirname(os.path.dirname(os.path.abspath(sys.executable)))
    torch_lib = os.path.join(venv, "Lib", "site-packages", "torch", "lib")
    lib_bin = os.path.join(venv, "Library", "bin")
    parts = [
        p for p in os.environ.get("PATH", "").split(os.pathsep)
        if p and "anaconda" not in p.lower() and "miniconda" not in p.lower()
    ]
    os.environ["PATH"] = os.pathsep.join([torch_lib, lib_bin, venv] + parts)
    if hasattr(os, "add_dll_directory"):
        for p in (torch_lib, lib_bin):
            if os.path.isdir(p):
                try:
                    os.add_dll_directory(p)
                except OSError:
                    pass


_harden_windows_dll_path()

SKILL_DIR = Path(__file__).resolve().parent
REF_DIR = SKILL_DIR / "references"
DB_DIR = SKILL_DIR / ".kb_index"
TABLE = "seo_geo"
EMBED_MODEL = "BAAI/bge-m3"

HEADER_RE = re.compile(r"^#{1,6}\s+(.*)$")
FM_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"')
    return fm, text[m.end():]


def chunk_markdown(title: str, body: str, max_chars: int) -> list[tuple[str, str]]:
    chunks: list[tuple[str, str]] = []
    cur: list[str] = []
    heading = title
    size = 0

    def flush():
        nonlocal cur, size
        text = "\n".join(cur).strip()
        if len(text) >= 30:
            chunks.append((heading, text))
        cur, size = [], 0

    for ln in body.splitlines():
        hm = HEADER_RE.match(ln)
        if hm:
            flush()
            heading = hm.group(1).strip() or heading
            continue
        cur.append(ln)
        size += len(ln) + 1
        if size > max_chars:
            flush()
    flush()
    return chunks


def main() -> None:
    ap = argparse.ArgumentParser(description="Build LanceDB semantic index over references/.")
    ap.add_argument("--max-chars", type=int, default=1800)
    ap.add_argument("--batch", type=int, default=16)
    args = ap.parse_args()

    import torch
    import lancedb
    from sentence_transformers import SentenceTransformer

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")

    records: list[dict] = []
    files = sorted(REF_DIR.rglob("*.md"))
    print(f"Reading {len(files)} markdown files ...")
    for md in files:
        raw = md.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(raw)
        title = fm.get("title", md.stem)
        category = md.relative_to(REF_DIR).parts[0]
        for ci, (heading, text) in enumerate(chunk_markdown(title, body, args.max_chars)):
            records.append(
                {
                    "embed_text": f"{title} > {heading}\n{text}",
                    "text": text,
                    "title": title,
                    "heading": heading,
                    "category": category,
                    "section": fm.get("section", ""),
                    "source_url": fm.get("source_url", ""),
                    "path": md.relative_to(SKILL_DIR).as_posix(),
                    "chunk": ci,
                }
            )
    print(f"Total chunks: {len(records)}")
    if not records:
        sys.exit("No chunks found. Scrape content first with scrape_seo_geo.py")

    print(f"Loading {EMBED_MODEL} ...")
    model = SentenceTransformer(EMBED_MODEL, device=device)
    texts = [r["embed_text"] for r in records]
    print("Embedding (this is the slow part) ...")
    vecs = model.encode(texts, batch_size=args.batch, normalize_embeddings=True, show_progress_bar=True)
    for r, v in zip(records, vecs):
        r["vector"] = v.tolist()
        del r["embed_text"]

    print(f"Writing LanceDB -> {DB_DIR}")
    db = lancedb.connect(str(DB_DIR))
    db.create_table(TABLE, data=records, mode="overwrite")
    print(f"Done. {len(records)} chunks indexed from {len(files)} docs.")


if __name__ == "__main__":
    main()
