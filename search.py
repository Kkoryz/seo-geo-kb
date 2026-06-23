#!/usr/bin/env python3
"""
Semantic search over the SEO/GEO knowledge base (same engine as klaviyo-marketing).

Two-stage retrieval: BGE-M3 dense recall (LanceDB) -> BGE reranker precision rerank.

Run with the klaviyo-marketing .venv:
    ~/.codex/skills/klaviyo-marketing/.venv/Scripts/python.exe \
      ~/.codex/skills/seo-geo-kb/search.py "如何为 AI 搜索优化产品页" --json -k 8
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass


def _harden_windows_dll_path() -> None:
    import os
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
DB_DIR = SKILL_DIR / ".kb_index"
TABLE = "seo_geo"
EMBED_MODEL = "BAAI/bge-m3"
RERANK_MODEL = "BAAI/bge-reranker-v2-m3"


def main() -> None:
    ap = argparse.ArgumentParser(description="Semantic search over the SEO/GEO KB.")
    ap.add_argument("query")
    ap.add_argument("-k", "--top", type=int, default=8)
    ap.add_argument("--recall", type=int, default=50)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--full", action="store_true")
    args = ap.parse_args()

    if not DB_DIR.exists():
        sys.exit("No index found. Run: index_kb.py")

    import torch
    import lancedb
    from sentence_transformers import SentenceTransformer, CrossEncoder

    device = "cuda" if torch.cuda.is_available() else "cpu"
    embedder = SentenceTransformer(EMBED_MODEL, device=device)
    qvec = embedder.encode([args.query], normalize_embeddings=True, show_progress_bar=False)[0]
    tbl = lancedb.connect(str(DB_DIR)).open_table(TABLE)
    cands = tbl.search(qvec.tolist()).limit(args.recall).to_list()
    if not cands:
        print("No results."); return

    reranker = CrossEncoder(RERANK_MODEL, device=device)
    scores = reranker.predict([[args.query, c["text"]] for c in cands], show_progress_bar=False)
    for c, s in zip(cands, scores):
        c["score"] = float(s)
    cands.sort(key=lambda c: c["score"], reverse=True)
    top = cands[: args.top]

    if args.json:
        print(json.dumps(
            [
                {
                    "score": round(c["score"], 4),
                    "title": c["title"],
                    "heading": c["heading"],
                    "category": c["category"],
                    "path": c["path"],
                    "source_url": c["source_url"],
                    "text": c["text"] if args.full else c["text"][:400],
                }
                for c in top
            ],
            ensure_ascii=False, indent=2,
        ))
        return

    print(f'\nQuery: {args.query}\nTop {len(top)} results:\n' + "=" * 60)
    for i, c in enumerate(top, 1):
        print(f"\n[{i}] score={c['score']:.3f}  ({c['category']})  {c['title']}")
        if c["heading"] and c["heading"] != c["title"]:
            print(f"    § {c['heading']}")
        print(f"    file: {c['path']}")
        if c["source_url"]:
            print(f"    url:  {c['source_url']}")
        body = c["text"] if args.full else (c["text"][:400] + ("..." if len(c["text"]) > 400 else ""))
        print("    " + body.replace("\n", "\n    "))


if __name__ == "__main__":
    main()
