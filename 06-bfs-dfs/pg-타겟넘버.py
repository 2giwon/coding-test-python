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
# 기저에서 이 갈래가 정답이면 1, 아니면 0을 반환하고, 부모는 두 갈래의 반환값을 더한다.
def solution_ref(numbers, target):
    def dfs(current, s):
        if current == len(numbers):
            return 1 if s == target else 0
        return dfs(current + 1, s + numbers[current]) + dfs(current + 1, s - numbers[current])

    return dfs(0, 0)


# 참고 정답 2: 완전탐색 관점 — 부호 조합 2^n개를 전부 생성해서 센다.
# DFS = "조합을 하나씩 생성하며 세는 것"임을 보여주는 대비. 실전은 DFS(가지치기 가능).
def solution_product(numbers, target):
    from itertools import product

    return sum(
        1
        for signs in product([1, -1], repeat=len(numbers))
        if sum(s * n for s, n in zip(signs, numbers, strict=True)) == target
    )


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
