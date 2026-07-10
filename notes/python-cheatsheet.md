# 코테용 Python 치트시트 (Kotlin 개발자 관점)

> 문제 풀다 막히면 여기부터. 새로 배운 패턴은 계속 추가한다.

## 입출력 (백준용 — 프로그래머스는 함수형이라 불필요)

```python
import sys
input = sys.stdin.readline          # 대량 입력 시 필수 (기본 input은 느림)
n = int(input())
a, b = map(int, input().split())
arr = list(map(int, input().split()))
```

## 컬렉션 — Kotlin 대응

```python
# listOf(1,2,3).map { it*2 }.filter { it > 2 }
[x * 2 for x in [1, 2, 3] if x * 2 > 2]

# mutableMapOf().getOrDefault / getOrPut
from collections import defaultdict, Counter
d = defaultdict(int); d["k"] += 1            # 없으면 0부터
Counter("hello")                              # 빈도 세기 한 방: {'l': 2, ...}
Counter(arr).most_common(3)                   # 상위 3개 (빈도순)

# ArrayDeque — BFS 큐는 반드시 deque (list.pop(0)은 O(n))
from collections import deque
q = deque([start]); q.append(x); q.popleft()

# PriorityQueue (최소 힙만 있음 — 최대 힙은 부호 반전)
import heapq
heapq.heappush(h, v); heapq.heappop(h)
heapq.heappush(h, -v)                         # 최대 힙 트릭
```

## 정렬

```python
arr.sort(key=lambda x: (-x[1], x[0]))   # 다중 키: 1번 내림차순, 0번 오름차순
sorted(d.items(), key=lambda kv: kv[1]) # dict 값 기준
```

## 자주 쓰는 관용구

```python
# 2차원 배열 초기화 ([[0]*m]*n 은 얕은복사 함정!)
grid = [[0] * m for _ in range(n)]

# 방향 벡터 (상하좌우)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# enumerate / zip (Kotlin withIndex / zip)
for i, v in enumerate(arr): ...
for a, b in zip(xs, ys): ...

# 조합/순열 (완전탐색 단골)
from itertools import combinations, permutations, product
combinations(arr, 2); permutations(arr); product([0, 1], repeat=n)

# 이분탐색
from bisect import bisect_left, bisect_right
idx = bisect_left(sorted_arr, target)

# 문자열 ↔ 아스키
ord("a"), chr(97)

# 몫/나머지, 거듭제곱
divmod(7, 3)      # (2, 1)
pow(a, b, mod)    # 모듈러 거듭제곱 내장
```

## 핵심 패턴: 집계(변환 for 원소 in 컬렉션)

파이썬 코테의 가장 흔한 뼈대. **안쪽(변환) → 바깥(집계)** 순서로 읽는다.
Kotlin의 `.map { }.maxOf/sumOf/any { }` 체인에 해당.

```python
max(max(s) for s in sizes)       # 각 명함의 긴 변 → 그중 최대 (최소직사각형)
sum(x**2 for x in nums)          # 각 원소 제곱 → 합
any(v > 0 for v in arr)          # 하나라도 양수? (Kotlin any)
all(c.isdigit() for c in s)      # 전부 숫자? (Kotlin all)
min(len(w) for w in words)       # 가장 짧은 단어 길이
sum(1 for x in arr if x % 2)     # 조건 세기 (count 대용)
```

- 소괄호 = 제너레이터(lazy, 리스트 안 만듦). 집계 함수에 바로 넣을 땐 이걸 쓴다
- 결과 자체가 필요하면 대괄호(리스트 컴프리헨션): `[max(s) for s in sizes]`

## 사고 패턴: 정규화(canonicalize) 먼저

**"회전/뒤집기/순서 무관" 조건이 보이면, 비교 로직에서 처리하지 말고 입력을 먼저 통일한다.**
정규화하면 조건 분기가 사라지고, 분기가 사라지면 놓치는 케이스도 사라진다.

```python
sorted(s)                        # 아나그램: 문자 순서 무관 → 정렬로 통일
(max(s), min(s))                 # 회전 가능 직사각형 → (긴 변, 짧은 변)으로 눕히기
tuple(sorted(pair))              # 무방향 간선 (a,b)==(b,a) → 정렬 튜플로 통일
```

> 출처: pg-최소직사각형 오답 — 회전 판단을 조건문으로 하려다 확장 시점 한 곳을 놓침
> (반례 `[[60,50],[30,70]]` → 4200 ≠ 3500). 정규화했으면 분기 자체가 없었다.

## 함정 목록 (당한 것 추가)

- `[[0]*m]*n` — 행이 전부 같은 객체 (얕은 복사)
- `list.pop(0)` O(n) — BFS는 `deque.popleft()`
- 재귀 기본 한도 1000 — `sys.setrecursionlimit(10**6)` (DFS 재귀 시)
- 정수 나눗셈 `//` 는 음수에서 내림 (Kotlin `/`은 0방향 절삭) — `int(-7/2) != -7//2`
- 기본 `input()` 느림 — 백준에서 TLE 원인
