#!/usr/bin/env python3
"""Create a new Jekyll post under _posts/ with the repo's standard frontmatter.

Usage (Windows: `python`, Mac: `python3`):
    python scripts/new_post.py
    python scripts/new_post.py -t "RNN과 Transformer 정리"
    python scripts/new_post.py project-x -t "포트폴리오용 프로젝트 X" -d 2026-09-10
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "_posts"


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\-]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "post"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new Jekyll post in _posts/")
    parser.add_argument("slug", nargs="?", default="skala", help="파일명에 쓸 슬러그 (기본: skala)")
    parser.add_argument("-t", "--title", help="포스트 제목 (기본: 'SKALA 학습 기록 - M월 D일')")
    parser.add_argument("-d", "--date", help="날짜 YYYY-MM-DD (기본: 오늘)")
    args = parser.parse_args()

    date = datetime.date.fromisoformat(args.date) if args.date else datetime.date.today()
    date_str = date.isoformat()
    title = args.title or f"SKALA 학습 기록 - {date.month}월 {date.day}일"
    slug = slugify(args.slug)

    filepath = POSTS_DIR / f"{date_str}-{slug}.md"
    if filepath.exists():
        sys.exit(f"이미 존재하는 파일입니다: {filepath}")

    content = f"""---
layout: post
title: "{title}"
date: {date_str}
tags: []
---

"""
    POSTS_DIR.mkdir(exist_ok=True)
    filepath.write_text(content, encoding="utf-8")
    print(f"생성됨: {filepath}")


if __name__ == "__main__":
    main()
