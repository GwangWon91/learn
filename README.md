# learn

## 새 글 쓰기

```bash
python scripts/new_post.py                          # 오늘 날짜, 기본 제목
python scripts/new_post.py -t "RNN과 Transformer"     # 제목 지정
python scripts/new_post.py project-x -t "포트폴리오 프로젝트" -d 2026-09-10  # 슬러그/날짜 지정
```

`_posts/`에 표준 frontmatter(layout, title, date, tags)를 갖춘 파일이 생성됩니다. Windows는 `python`, Mac은 `python3`.
