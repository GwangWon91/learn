# learn

## 새 글 쓰기

```bash
python scripts/new_post.py                          # 오늘 날짜, 기본 제목
python scripts/new_post.py -t "RNN과 Transformer"     # 제목 지정
python scripts/new_post.py project-x -t "포트폴리오 프로젝트" -d 2026-09-10  # 슬러그/날짜 지정
```

`_posts/`에 표준 frontmatter(layout, title, date, tags)를 갖춘 파일이 생성됩니다. Windows는 `python`, Mac은 `python3`.

## 구조

- `/` — 학습 로그(포스트) 목록
- `/about/` — 소개
- `/projects/` — 포트폴리오 프로젝트 목록 (`_projects/` 컬렉션)
- `/tags/` — 태그별 글 모아보기

새 프로젝트를 추가하려면 `_projects/`에 `_projects/example-project.md`를 참고해서 파일을 만들고 `published: false`를 지우면 됩니다.
