# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 핵심: N/2마리만 데려갈 수 있고 최대한 다양하게 → 답 = min(N//2, 폰켓몬 종류 수).
#       종류 수 = len(set(nums)). N은 항상 짝수라 //로 딱 떨어짐.
# 리뷰: 로직은 처음부터 정답. 함정은 나눗셈 타입 — len(nums)/2는 float(2.0)를 줘서
#       개수인데 실수가 반환됨(프로그래머스는 2.0==2라 통과시키지만 부정확).
#       교훈: "개수/인덱스는 정수" → 몫만 필요하면 // (정수 나눗셈). / 는 항상 float.


def solution(nums):
    kinds = set(nums)  # set이 중복 자동 제거 → 폰켓몬 종류
    pick = len(nums) // 2  # 데려갈 수 있는 마리 수 (정수!)
    return min(len(kinds), pick)


if __name__ == "__main__":
    assert solution([3, 1, 2, 3]) == 2  # 종류 3 > 2마리 → 2
    assert solution([3, 3, 3, 2, 2, 4]) == 3  # 종류 3 = 3마리 → 3
    assert solution([3, 3, 3, 2, 2, 2]) == 2  # 종류 2 < 3마리 → 2
    print("all passed")
