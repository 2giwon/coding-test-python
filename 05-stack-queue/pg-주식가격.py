# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 핵심: 각 시각 i의 답 = "i 뒤에서 처음으로 prices[i]보다 싼 가격이 나오는 시각 j"까지의 거리
#       (j - i). 끝까지 안 싸지면 마지막 시각까지의 거리(n-1-i). 같은 가격은 '떨어진 것'이 아님.
# 리뷰: 20분 자력 통과 — 이중 루프(i마다 뒤를 훑고 싸지면 break). O(n²)라 가격이 계속 오르는
#       입력(n=10만)이면 break가 안 걸려 ~50억 비교 → 프로그래머스는 통과했지만 실전 채점기 위험.
#       처음엔 리스트에 값을 쌓아 len()으로 셌는데 실질은 카운터라 정리 시 카운터로 교체.
#       스택 O(n) 풀이(solution_ref)는 아직 이해 미완 → 1주 후 스택 방식으로 재도전 [재풀이: 09/14]


def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i + 1, len(prices)):
            count += 1  # 떨어지는 그 초도 "버틴 기간"에 포함되므로 비교 전에 센다
            if prices[i] > prices[j]:
                break
        answer.append(count)
    return answer


# 참고 정답: 스택 O(n) — "미래를 뒤지지" 말고 "답을 못 받은 시각들을 대기시킨다".
#
# 발상: 시각 j를 왼쪽부터 한 번만 지나간다. 아직 "떨어지는 순간"을 못 만난 시각들을
# 스택(대기 명단)에 인덱스로 적어둔다. 새 시각 j의 가격이 나오면, 명단에서 j보다 비싼
# 시각들은 "바로 지금(j) 떨어졌다" → 답 = j - i 를 적고 명단에서 뺀다.
#
# 왜 맨 위만 확인하면 되나: 명단은 항상 아래가 싸고 위가 비싼 상태다 (j보다 비싼 것들을
# 전부 뺀 뒤에 j를 올리니까). 그래서 맨 위부터 확인하다 "안 떨어지는 것"을 만나면
# 그 아래는 더 싸서 전부 안 떨어진다 → 거기서 멈춰도 된다.
#
# 추적 [1,2,3,2,3]  (표기 idx:가격)
#   j=0 가격1: 명단 비어있음 → 올림          명단 [0:1]
#   j=1 가격2: 맨위 0:1 > 2? 아니오 → 올림     명단 [0:1, 1:2]
#   j=2 가격3: 맨위 1:2 > 3? 아니오 → 올림     명단 [0:1, 1:2, 2:3]
#   j=3 가격2: 맨위 2:3 > 2? 예 → answer[2]=3-2=1, 뺌
#              맨위 1:2 > 2? 아니오(같음=유지) → 멈춤, 3 올림   명단 [0:1, 1:2, 3:2]
#   j=4 가격3: 맨위 3:2 > 3? 아니오 → 올림     명단 [0:1, 1:2, 3:2, 4:3]
#   끝. 남은 명단은 끝까지 안 떨어진 시각들 → answer[i] = 4 - i  → 4, 3, 1, 0
#   결과 [4, 3, 1, 1, 0]
#
# 각 인덱스는 명단에 한 번 들어가고 한 번 나가므로 전체 O(n).
def solution_ref(prices):
    n = len(prices)
    answer = [0] * n
    stack = []  # 아직 답을 못 받은 시각(인덱스)들의 대기 명단
    for j in range(n):
        while stack and prices[stack[-1]] > prices[j]:  # 맨 위 대기자보다 싸졌다 = 떨어졌다
            i = stack.pop()
            answer[i] = j - i  # i초에 산 사람은 j초에 떨어짐 → j-i초 버팀
        stack.append(j)
    for i in stack:  # 끝까지 안 떨어진 시각들
        answer[i] = n - 1 - i
    return answer


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 2, 3], [4, 3, 1, 1, 0]),
        ([5, 4, 3, 2, 1], [1, 1, 1, 1, 0]),  # 매초 떨어지는 경우
        ([1, 1, 1], [2, 1, 0]),  # 같은 가격 = 떨어진 게 아님
        ([1, 2, 3, 4, 5], [4, 3, 2, 1, 0]),  # 계속 오름 — 이중 루프의 최악 케이스
    ]
    for prices, expected in cases:
        assert solution(prices) == expected
        assert solution_ref(prices) == expected
    print("모든 케이스 통과 (이중 루프 + 스택 참고 정답)")
