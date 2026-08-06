# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 핵심: 조합을 "만들지" 말고 "세기". 각 종류(k개)의 선택지 = k+1 (하나 입기 k + 안 입기 1).
#       모든 종류의 (k+1)을 곱하고, "전부 안 입기" 1가지를 뺀다. → 곱의 법칙, O(n).
# 리뷰: 처음 모든 조합을 실제로 생성하려다 시간 초과(2^n). 조합 문제인데 조합을 안 만드는 게 정답.
#       교훈: "경우의 수"는 나열 말고 곱셈으로 세라(모음사전 가중치와 같은 결).
#       Counter로 종류별 개수 집계 → 지난주 배운 도구 재사용.
from collections import Counter


def solution(clothes):
    # clothes = [[이름, 종류], ...]. 이름은 유일 → dict로 {이름: 종류}, values()가 종류 나열
    category_counts = Counter(dict(clothes).values())  # 종류별 아이템 수
    answer = 1
    for count in category_counts.values():
        answer *= count + 1  # 그 종류: 하나 입기(count) + 안 입기(1)
    return answer - 1  # "전부 안 입기" 1가지 제외


if __name__ == "__main__":
    assert (
        solution(
            [
                ["yellow_hat", "headgear"],
                ["blue_sunglasses", "eyewear"],
                ["green_turban", "headgear"],
            ]
        )
        == 5
    )
    assert (
        solution(
            [
                ["crow_mask", "face"],
                ["blue_sunglasses", "face"],
                ["smoky_makeup", "face"],
            ]
        )
        == 3
    )
    print("all passed")
