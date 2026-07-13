# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 핵심: 숫자 조각으로 만들 수 있는 모든 수(순열) 생성 → int 정규화 후 set 중복 제거 → √n 소수 판별
#       조립 라인: "뽑고(permutations) → 붙이고(join) → 숫자로(int) → 담고(set) → 세기"
# 리뷰: 07/12 시간 초과(순열 손 구현) → 풀이 학습. 교훈①: "모든 경우의 수" = itertools 반사.
#       07/13 재현 제출: 문자열인 채 set에 담아 "11"과 "011"이 따로 카운트되는 오답
#       (공식 예제 "011"→3≠2). 교훈②: 중복 제거는 정규화(int) "후에" — set에 뭘 담는지가 관건.
#       수정 재제출 통과. 재귀(백트래킹) 버전은 git 이력과 치트시트 참조.
#       [재풀이: 07/20 — 조립 라인 안 보고 재현이 과녁]
from itertools import permutations


def is_prime(num):
    if num < 2:
        return False

    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False

    return True


def solution(numbers):
    cases = set()

    for c in range(1, len(numbers) + 1):  # 1자리부터 전체 자리까지 (k=0 빈 순열 배제)
        for p in permutations(numbers, c):
            number = int("".join(p))  # 튜플 → 문자열 → 숫자 정규화 후에 담는다
            cases.add(number)

    count = 0
    for case in cases:
        if is_prime(case):
            count += 1

    return count


if __name__ == "__main__":
    # 로컬 검증 (공식 예제 + 오답 반례)
    print(solution("17"))  # 3 (7, 17, 71)
    print(solution("011"))  # 2 (11, 101) ← 문자열 dedup 버그를 잡아준 케이스
    print(solution("010"))  # 0 — 1이 하나뿐이라 11/101 불가
    print(solution("100"))  # 0 ("010"과 같은 재료)
    print(solution("175"))  # 7 (5, 7, 17, 71, 157, 571, 751)
