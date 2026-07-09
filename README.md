# coding-test-python

프로그래머스/백준 코딩 테스트 풀이 + 오답 노트 (Python 3.13)

> 26주 코테 트랙의 실행 리포. 전략/로드맵: [career-transition/curriculum/02-coding-test.md](https://github.com/2giwon/career-transition)

## 구조

```
01-implementation/   구현·완전탐색
02-string/           문자열·정규식
03-hash/             해시
04-sort/             정렬
05-stack-queue/      스택·큐·투포인터
06-bfs-dfs/          BFS/DFS
07-graph/            그래프 (최단거리, 유니온파인드)
08-dp/               동적 계획법
09-greedy/           그리디·이분탐색
10-binary-search/    이분탐색
notes/               유형별 패턴 정리, 파이썬 치트시트
```

## 파일 규칙

- 파일명: `{플랫폼}-{문제명}.py` (예: `pg-모의고사.py`, `boj-1260.py`)
- 파일 상단 주석 3줄:
  ```python
  # 문제: (URL)
  # 핵심: (한 줄 아이디어)
  # 리뷰: (막힌 지점 — 안 막혔으면 생략) [재풀이: MM/DD]
  ```

## 운영 룰

1. 매일 최소 1문제 — 25분 타이머, 실전처럼
2. 25분 내 접근법이 안 나오면 풀이 확인 → **다음날 재풀이** (`리뷰:` 주석에 기록)
3. 풀었어도 다른 사람 풀이 1개 읽고 더 파이썬다운 방법 확인
4. 막혔던 문제는 1주 후 재풀이

## 도구

```bash
uv run python 01-implementation/pg-모의고사.py   # 실행
ruff check . && ruff format .                    # 린트 + 포맷
```
