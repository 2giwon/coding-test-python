# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 핵심: 전체 타일 수(brown+yellow)의 약수 쌍을 √n까지 순회 → 각 쌍에서 테두리(-2) 제거한
#       내부가 yellow와 일치하면 정답. 곱이 주어지면 √n 약수 쌍, 기하 제약은 좌표 변환으로 축소.
# 리뷰: 첫 자력 해결 (07/13, 풀이 참조 없음). 소수찾기에서 배운 "약수는 짝(√n)" 패턴을 전이 적용.
#       제출 전 다듬기 3건: 디버그 print 제거 / i≤√n이라 case[0]≤case[1] 보장 → max/min 불필요,
#       답 유일(합·곱 고정)이라 즉시 return / int(x**0.5) + 1 관례.

# 나의 생각
# 2개의 수를 더한 뒤
# 그 수의 약수들을 구함 = ex 10 + 2 = 12 = 1 * 12, 2 * 6, 3 * 4
# 그 수들에서 2씩 빼서 yellow의 수가 나올 수 있는지 판단
# 1, 12는 안됨
# 2, 6도 안됨 (2씩 빼면 0됨)
# 4, 3 (가로가 더 길어야 하기 때문) 4 - 2 = 2, 3 - 2 = 1 => yellow => 2 * 1 = 2 가능
def solution(brown, yellow):
    sumValue = brown + yellow
    cases = []  # ruff C408: list()보다 리터럴 [] 이 관례

    for i in range(1, int(sumValue**0.5) + 1):
        if sumValue % i == 0:
            case = [i, sumValue // i]
            cases.append(case)

    for case in cases:
        a = case[0] - 2
        b = case[1] - 2

        if a > 0 and b > 0 and a * b == yellow:
            return [case[1], case[0]]


if __name__ == "__main__":
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(24, 24))
