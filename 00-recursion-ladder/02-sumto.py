# 재귀 사다리 2번 (08/06 통과): 1+2+...+n
# 교훈: ①종료조건은 "답을 아는 지점"이 아니라 "모든 입력이 반드시 도달하는 지점" — n==1이면
#       0·음수가 무한 재귀 → n <= 0 (부등호가 안전). ②수선 중 n <= 1로 잡아 1까지 삼키는
#       off-by-one 발생(sumto(5)=14) — 경계 수정 후엔 반드시 재실행 + assert로 검증.


def sumto(n):
    if n <= 0:  # 0·음수까지 안전 (아무것도 안 더한 합 = 0)
        return 0
    return n + sumto(n - 1)


if __name__ == "__main__":
    assert sumto(5) == 15
    assert sumto(1) == 1  # 경계: n <= 1로 잡으면 여기서 깨진다
    assert sumto(10) == 55
    assert sumto(0) == 0
    assert sumto(-3) == 0
    print("all passed")
