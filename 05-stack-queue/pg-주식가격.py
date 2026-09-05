# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 핵심:
# 리뷰:


def solution(prices):
    answer = []

    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
    print(solution([5, 4, 3, 2, 1]))  # [1, 1, 1, 1, 0] — 매초 떨어지는 경우
    print(solution([1, 1, 1]))  # [2, 1, 0] — "가격이 떨어지지 않은" = 같아도 유지
