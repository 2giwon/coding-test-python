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

## 사고 패턴: "모든 경우의 수"가 보이면 itertools 반사

직접 만들지 말 것. 손 구현하다 시간 초과가 소수 찾기(42839)의 실패 원인이었다.

```python
from itertools import permutations, combinations, product

permutations("175", 2)   # 순서 있음: 17, 71, 15, 51, 75, 57 (2자리 배열)
combinations([1,2,3], 2) # 순서 없음: (1,2), (1,3), (2,3) (짝 뽑기)
product([0,1], repeat=3) # 중복 허용 전체 조합: 000, 001, ... 111 (2^3)
```

- 고르는 것에 **순서가 의미 있으면** permutations, **없으면** combinations
- 만든 결과의 중복 제거는 `set`으로 (예: "011" → int 변환하면 같은 수가 여러 번)
- **조립 라인 암기: "뽑고 → 붙이고 → 숫자로 → 담고 → 세기"** (07/13 재현 때 막힌 지점)

```python
candidates = set()
for k in range(1, len(numbers) + 1):
    for p in permutations(numbers, k):   # 뽑고 — 결과는 튜플 ('7','1')!
        candidates.add(int("".join(p)))  # 붙이고(join) → 숫자로(int) → 담고(set)
count = sum(1 for n in candidates if is_prime(n))  # 세기
# 함정: permutations는 문자열이 아니라 "튜플"을 준다 → "".join()이 다리 (Kotlin joinToString)
```

## 부품: 소수 판별 (√n까지만)

**약수는 짝으로 다니고, 짝의 작은 쪽은 √n을 못 넘는다** (둘 다 √n보다 크면 곱이 n을
초과). 그래서 √n까지 뒤져서 없으면 그 위에도 없다. 9,999,999도 3,162번이면 끝.

```python
def is_prime(n):
    if n < 2:                              # 0, 1은 소수 아님 (이 가드 필수!)
        return False
    for d in range(2, int(n**0.5) + 1):    # n**0.5 = √n, range라 +1
        if n % d == 0:
            return False
    return True
```

- 함정: 확인은 **2부터** (1로 나누면 모든 수가 걸러짐), `n < 2` 가드 누락

## 사고 패턴: 재귀 = "계약으로 읽기" (완전탐색/DFS/백트래킹의 뼈대)

머리로 호출을 펼치지 말 것. 함수 = 계약("이 상태에서 나머지를 전부 처리해준다")으로
읽고, 지금 층의 로직만 확인한다. 구조는 항상 3요소:

```python
def explore(remaining, current):
    if current:                              # ① 현재 상태 처리 (등록/판정)
        candidates.add(int(current))
    for i in range(len(remaining)):          # ② 가능한 선택지 순회
        rest = remaining[:i] + remaining[i+1:]   # i번째만 뺀 나머지 (새 문자열)
        explore(rest, current + remaining[i])    # ③ 작아진 문제는 재귀에 위임
    # 종료 조건: remaining이 ""이면 for가 0바퀴 → 자연 종료 (암묵적 base case)
```

- **선택 → 재귀 → 복귀(다음 선택)** — 이 복귀가 곧 백트래킹
- 문자열/튜플은 불변이라 새로 만들어 넘기면 **상태 복원 코드가 필요 없음**
  (공유 리스트를 쓰면 `append → 재귀 → pop`으로 직접 복원 — W13에서)
- 이해 안 되면 `depth` 파라미터 + 들여쓰기 print로 **컴퓨터한테 펼치게** 한다:

```python
def explore(remaining, current, depth=0):
    print("    " * depth + f"({remaining!r}, {current!r})")
    ...
    explore(rest, current + picked, depth + 1)
```

## 사고 패턴: 규모를 먼저 세라 — 나열 vs 수식

**"모든 경우"가 보이면 먼저 개수를 계산한다.** 그 규모에 따라 무기가 갈린다.

- 규모가 작으면(수천~수십만) → **통째로 나열**(product/재귀)하고 index. 계산하지 말고 만들어라.
- 규모가 크거나 index가 필요없으면 → **수식으로 건너뛰라**(가중치). 전체 생성 없이 O(len).

```python
# 모음사전(84512): 각 자리가 대표하는 서브트리 크기 = 가중치
# 점화식: 앞 자리 가중치 × 5 + 1  → [781, 156, 31, 6, 1]
#   (한 자리 더 붙이면 5갈래 생기고(×5) + 자기 자신 1개(+1))
weights = [781, 156, 31, 6, 1]
rank = sum(weights[i] * "AEIOU".index(ch) for i, ch in enumerate(word)) + len(word)
```

- 전체 나열(product/재귀)과 가중치 계산은 **같은 트리를 나열하느냐 수식으로 세느냐**의 차이
- 가변 깊이 나열의 근본은 재귀 → notes/recursion.md (반드시 체득)

## 함정 목록 (당한 것 추가)

- `[[0]*m]*n` — 행이 전부 같은 객체 (얕은 복사)
- `list.pop(0)` O(n) — BFS는 `deque.popleft()`
- 재귀 기본 한도 1000 — `sys.setrecursionlimit(10**6)` (DFS 재귀 시)
- 정수 나눗셈 `//` 는 음수에서 내림 (Kotlin `/`은 0방향 절삭) — `int(-7/2) != -7//2`
- 기본 `input()` 느림 — 백준에서 TLE 원인
