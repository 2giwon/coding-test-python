# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 핵심: 숫자 조각으로 만들 수 있는 모든 수(순열) 생성 → set 중복 제거 → √n 소수 판별
# 리뷰: 07/12 시간 초과(순열 손 구현) → 풀이 학습. 교훈: "모든 경우의 수" = itertools 반사.
#       07/13 재현 제출 통과. 막힌 지점: permutations 결과(튜플)→join→int→set→sum 조립 라인
#       ("뽑고→붙이고→숫자로→담고→세기", 치트시트 등재). 이 파일은 재귀 버전 기록.
#       [재풀이: 07/20 — 조립 라인 안 보고 재현이 과녁]
def solution(numbers):
    candidates = set()

    def explore(remaining, current):
        # remaining: 아직 안 쓴 숫자 조각들, current: 지금까지 만든 수 (문자열)
        if current:  # 빈 문자열이 아니면
            candidates.add(int(current))  # 지금까지 만든 수를 후보에 등록

        for i in range(len(remaining)):
            picked = remaining[i]  # i번째 조각을 뽑고
            rest = remaining[:i] + remaining[i + 1 :]  # 그걸 뺀 나머지
            explore(rest, current + picked)  # 나머지로 같은 문제 반복

    explore(numbers, "")
    return sum(1 for n in candidates if is_prime(n))  # is_prime은 아까 그대로


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    # print로 감싸야 결과가 보인다 (solution만 호출하면 반환값이 버려짐)
    print(solution("17"))  # 3 (7, 17, 71)
    print(solution("011"))  # 2 (11, 101)
    print(solution("010"))  # 0 — 1이 하나뿐이라 11/101 불가, {0,1,10,100} 전부 소수 아님
    print(solution("100"))  # 0 ("010"과 같은 재료)
    print(solution("175"))  # 7 (5, 7, 17, 71, 157, 571, 751)
