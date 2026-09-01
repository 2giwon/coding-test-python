# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 핵심: "크기 순"이 아닌 **"앞에 붙였을 때 커지는 순"** — 커스텀 정렬 기준을 만드는 문제.
#       a가 b보다 앞 ⟺ a+b > b+a (붙여보고 비교). 이를 key=lambda x: x*3 (문자열 반복)로 구현 —
#       원소가 최대 1000(4자리)이라 3번 반복이면 무한 반복 비교와 동치. O(n log n).
#       일반해는 functools.cmp_to_key(a+b vs b+a) — 제약 무관하게 성립.
# 리뷰: 첫 시도 permutations 완전탐색 → n 최대 100,000 = n! 폭발로 런타임에러+시간초과.
#       교훈①: "모든 경우"가 보이면 개수부터 세라 (n>10이면 순열 나열은 죽음).
#       교훈②: 전부 0 함정 — lstrip("0")은 빈 문자열이 됨. str(int())는 파이썬 3.11+에서
#       4300자리 제한으로 터질 수 있는 환경 의존 코드(채점기 구버전이라 통과할 뿐).
#       → 내림차순 1등이 "0"이면 전부 0이라는 논리 체크가 어디서나 안전한 정석.
#       교훈③: 같은 코드도 환경(버전)에 따라 통과/실패 — 남의 통과 코드 ≠ 내 환경에서 안전.


def solution(numbers):
    strNumbers = list(map(str, numbers))
    strNumbers.sort(key=lambda x: x * 3, reverse=True)  # 붙였을 때 커지는 순
    if strNumbers[0] == "0":  # 내림차순 1등이 0 = 전부 0
        return "0"
    return "".join(strNumbers)


if __name__ == "__main__":
    assert solution([6, 10, 2]) == "6210"
    assert solution([3, 30, 34, 5, 9]) == "9534330"
    assert solution([0, 0, 0, 0]) == "0"  # 전부 0 함정
    assert solution([0]) == "0"
    assert solution([1000, 999]) == "999" + "1000"  # 자릿수 다른 비교
    print("all passed")
