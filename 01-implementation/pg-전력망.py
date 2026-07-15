# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 핵심: [W5 보류] 전선 하나씩 끊어보기(완전탐색, ≤100개)까지는 도달 — 끊은 뒤 두 그룹
#       크기를 세는 "그래프 순회(BFS/DFS)"가 필요해서 보류. W5에서 배우는 도구.
# 리뷰: 07/15 시도 — 아이디어 절반(끊어보기)은 자력 도달, 나머지 절반은 미학습 영역이라
#       계획된 이관. [W5 재도전: 피로도 DFS 버전과 같은 날 묶어서]


def solution(n, wires):
    answer = -1
    return answer


if __name__ == "__main__":
    print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
    print(solution(4, [[1, 2], [2, 3], [3, 4]]))
    print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
