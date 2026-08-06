# 재귀 사다리 1번 (08/05 통과): n!
# 교훈: base case n == 0 → 1 (0! = 1 정의까지 커버). 음수는 무한 재귀 — 종료조건 도달 범위 의식.


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    assert factorial(5) == 120
    assert factorial(4) == 24
    assert factorial(3) == 6
    assert factorial(0) == 1  # 0! = 1
    print("all passed")
