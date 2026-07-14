# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 핵심: 던전 순서 전체 순열(n≤8 → 8!=40,320) 완전탐색 — 순열마다 시뮬레이션해 최대 탐험 수.
#       못 가는 던전은 스킵해도 과대계산 없음(스킵 결과 = 다른 순열이 커버하는 유효 순서).
# 리뷰: 자력 해결 (07/14). itertools 반사 이틀 연속 적용. 다듬기: permutations 직접 순회(리스트
#       변환 불필요), 상태(count)는 사용 직전 초기화, 만점 도달 시 조기 종료(가지치기).
#       [W5 재도전: DFS/백트래킹(visited 배열) 버전으로 다시 풀기 — 정석 비교]

# 나의 생각
# 모든 경우의 수를 구해서
# 예를 들면 (
# ([80, 20], [50, 40], [30, 10])
# ([80, 20], [30, 10], [50, 40]),
# ([50, 40], [80, 20], [30, 10]),
# ([50, 40], [30, 10], [80, 20]),
# ([30, 10], [50, 40], [80, 20]),
# ([30, 10], [80, 20], [50, 40]),
# )
# 각 경우의 수에 피로도를 계산하여 가장 높은 탐험수를 구한다
from itertools import permutations


def solution(k, dungeons):
    answer = -1

    for cases in permutations(dungeons):
        if answer == len(dungeons):
            break

        count = 0
        expectK = k
        for dungeon in cases:
            if expectK >= dungeon[0]:
                expectK -= dungeon[1]
                count += 1

        answer = max(answer, count)

    return answer


if __name__ == "__main__":
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))
