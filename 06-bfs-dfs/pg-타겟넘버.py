# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 핵심: 결정 트리 DFS — 숫자마다 +/− 두 갈래, dfs(몇 번째 결정, 지금까지의 합).
#       기저 조건 = 숫자를 다 썼을 때 합이 target인지 판정. "모든 경우의 수" 신호 → DFS.
#       visited 불필요 (결정 트리는 되돌아갈 수 없는 구조). 2^20 ≈ 100만이라 완전탐색 OK.
# 리뷰: 27분 자력 통과 (DFS/BFS 첫 문제, 힌트 없음). count를 인자로 들고 다니는 누산기
#       방식으로 풀었는데, 재귀의 표준형은 "각 갈래가 자기 몫을 반환하고 부모가 더한다"
#       (solution_ref) — 인자 하나 줄고 기저 조건도 하나로 합쳐진다. [재풀이: 09/15]


def solution(numbers, target):
    def dfs(current, s, count):
        if current == len(numbers):
            return count + 1 if s == target else count

        count = dfs(current + 1, s + numbers[current], count)
        count = dfs(current + 1, s - numbers[current], count)
        return count

    return dfs(0, 0, 0)


# 참고 정답 1: 반환값 합산형 DFS — "경우의 수 세기"의 표준형.
# 핵심 아이디어: 각 갈래(함수 호출)가 "내 아래에서 정답이 몇 개 나왔나"를 숫자로 반환한다.
# 맨 끝 갈래는 정답이면 1, 아니면 0. 부모는 두 자식이 돌려준 숫자를 더해서 자기 부모에게
# 돌려준다. 그래서 값이 나무 아래에서 위로 올라오며 합쳐지고, 맨 위(dfs(0,0))가 총 개수가 된다.
#
# 예: numbers=[1,1], target=0
#   dfs(0, 0)                                 ← 최종 답 = 1 + 1 = 2
#   ├─ +1 → dfs(1, 1)                         ← 0 + 1 = 1
#   │       ├─ +1 → dfs(2, 2) : 다 썼고 2≠0 → 0
#   │       └─ -1 → dfs(2, 0) : 다 썼고 0==0 → 1
#   └─ -1 → dfs(1, -1)                        ← 1 + 0 = 1
#           ├─ +1 → dfs(2, 0) : 다 썼고 0==0 → 1
#           └─ -1 → dfs(2, -2): 다 썼고 -2≠0 → 0
def solution_ref(numbers, target):
    n = len(numbers)

    def dfs(current, s):
        # current: 지금 몇 번째 숫자에 부호를 붙일 차례인가 (0부터 시작)
        # s: 지금까지 부호를 붙여 더한 합

        # [기저 조건] 숫자를 전부 썼다 → 이 갈래는 여기서 끝.
        # 정답인지만 판정해서 개수(0 또는 1)를 반환한다
        if current == n:
            if s == target:
                return 1  # 이 갈래는 정답 1개
            else:
                return 0  # 이 갈래는 정답 아님

        # [갈림길] 아직 숫자가 남았다 → 현재 숫자에 +를 붙인 세계와 -를 붙인 세계로 각각 내려간다
        # +를 붙였을 때, 그 아래에서 나온 정답 개수
        plus_count = dfs(current + 1, s + numbers[current])
        # -를 붙였을 때, 그 아래에서 나온 정답 개수
        minus_count = dfs(current + 1, s - numbers[current])

        # 두 세계의 정답 개수를 합친 것이 "이 지점 아래의 정답 개수"
        return plus_count + minus_count

    return dfs(0, 0)  # 0번째 숫자부터, 합 0에서 시작


# 참고 정답 2: 완전탐색 관점 — 부호 조합 2^n개를 전부 만들어보고 target이 되는 것을 센다.
# DFS가 "조합을 하나씩 생성하며 세는 것"과 같다는 걸 보여주는 대비. 실전은 DFS(가지치기 가능).
def solution_product(numbers, target):
    from itertools import product

    n = len(numbers)
    count = 0

    # product([1, -1], repeat=n): 길이 n짜리 부호 조합을 전부 만들어준다
    # 예: n=2 → (1, 1), (1, -1), (-1, 1), (-1, -1)  — 총 2^n개
    for signs in product([1, -1], repeat=n):
        total = 0
        for i in range(n):
            total += signs[i] * numbers[i]  # i번째 부호 × i번째 숫자
        if total == target:
            count += 1

    return count


if __name__ == "__main__":
    cases = [
        (([1, 1, 1, 1, 1], 3), 5),
        (([4, 1, 2, 1], 4), 2),
        (([1], 1), 1),  # 숫자 1개, +만 가능
        (([1], 2), 0),  # 만들 수 없음
    ]
    for (numbers, target), expected in cases:
        assert solution(numbers, target) == expected
        assert solution_ref(numbers, target) == expected
        assert solution_product(numbers, target) == expected
    print("모든 케이스 통과 (누산기 DFS + 합산 DFS + product)")
