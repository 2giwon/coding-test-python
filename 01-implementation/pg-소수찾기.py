# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 핵심: 숫자 조각으로 만들 수 있는 모든 수(순열) 생성 → set 중복 제거 → √n 소수 판별
# 리뷰: [학습본 — 풀이 보고 옮겨 적음, 미제출] 25분 내 접근 설계(경우의 수→소수→카운트)는
#       정답과 동일했으나 순열 손 구현에서 시간 초과. 교훈: "모든 경우의 수" = itertools 반사.
#       이 파일은 재귀 버전. [재현 도전: 07/13 itertools 버전으로 안 보고 작성→제출]
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
    print(solution("010"))  # 2 ("011"과 같은 재료)
    print(solution("100"))  # 0 (1, 10, 100, 세 자리 조합 모두 소수 아님)
    print(solution("175"))  # 12
