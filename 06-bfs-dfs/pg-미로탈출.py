# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/159993
# 핵심: 레버 필수 → 답 = (S→L 최단 이동) + (L→E 최단 이동). 하나라도 못 가면 -1.
#       "통로를 여러 번 지날 수 있다"는 조건이 두 구간을 독립적으로 풀어 더하는 것을 정당화한다
#       (구간끼리 칸을 다투지 않으므로). BFS를 함수로 빼면 방문 표가 호출마다 새로 생겨
#       구간 분리가 공짜로 따라온다 — 이게 함수화의 진짜 이유.
# 리뷰: 25분 초과 + 힌트 4단계(구조만) 후 자력 완성. 막혔던 4가지 =
#       ①S/L/E 좌표 찾기 ②BFS를 함수로 빼기 ③두 구간 더하기 ④방문 표를 새로 만들기.
#       🔴 최대 함정: 이 문제는 "칸 수"가 아니라 "이동 횟수"라 출발점이 0.
#          게임 맵의 `dist > 0` 방문 체크를 그대로 쓰면 출발점이 미방문으로 보여 무한 루프
#          (1차 시도의 시간 초과 원인). → 미방문을 -1로 두고 `dist[nr][nc] > -1` 로 체크.
#       🔴 두 번째 교훈: break 는 가장 안쪽 루프 하나만 빠져나온다. 목표 도착 시 while 까지
#          끝내려면 return (solution_ref 참고). 좌표 찾기 for 에서도 같은 혼동이 있었다.
#       [재풀이 완료: 09/16 — 19분 자력 통과. 결과는 pg-미로탈출-재풀이.py 참조]
from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])

    # ① S / L / E 좌표 찾기 — 한 번 훑으며 셋을 동시에, 튜플로 저장
    start = lever = goal = None
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "E":
                goal = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)

    # ② BFS 함수 — src 에서 dst 까지 최소 이동 횟수 (못 가면 -1)
    def bfs(src, dst):
        # ④ dist 표를 함수 안에서 만든다 → 호출마다 새로 생김. 미방문 = -1, 출발점 = 0
        dist = [[-1 for _ in range(m)] for _ in range(n)]
        sr, sc = src
        dist[sr][sc] = 0

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        dstr, dstc = dst
        visited_queue = deque([src])
        while visited_queue:
            r, c = visited_queue.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nc < 0 or nr >= n or nc >= m:
                    continue
                if maps[nr][nc] == "X" or dist[nr][nc] > -1:
                    continue
                if dstr == nr and dstc == nc:
                    dist[nr][nc] = dist[r][c] + 1
                    break  # 🔴 for 만 끊는다 — while 은 계속 돈다 (정답은 나오나 낭비)

                dist[nr][nc] = dist[r][c] + 1
                visited_queue.append((nr, nc))

        return dist[dstr][dstc]

    leverTime = bfs(start, lever)
    goalTime = bfs(lever, goal)
    # ③ 두 구간 계산해서 더하기
    return -1 if leverTime < 0 or goalTime < 0 else leverTime + goalTime


# 참고 정답: 위와 논리는 같고 두 곳이 다르다.
#   (1) 목표 판정을 "큐에서 꺼낼 때" 하고 break 대신 return → 도착하면 함수가 즉시 끝난다.
#       본 풀이는 목표를 찾은 뒤에도 남은 큐를 전부 소진한다(dist 를 덮어쓰지 않아 답은 맞지만,
#       더 큰 격자에서는 헛일). break 는 가장 안쪽 루프만, return 은 함수 전체를 끝낸다.
#   (2) 목표 좌표를 미리 풀어둘 필요가 없어져 dstr/dstc 와 목표 판정 if 블록이 사라진다.
def solution_ref(maps):
    n, m = len(maps), len(maps[0])

    start = lever = goal = None
    for r in range(n):
        for c in range(m):
            if maps[r][c] == "S":
                start = (r, c)
            elif maps[r][c] == "L":
                lever = (r, c)
            elif maps[r][c] == "E":
                goal = (r, c)

    def bfs(src, dst):
        dist = [[-1] * m for _ in range(n)]
        sr, sc = src
        dist[sr][sc] = 0
        q = deque([src])

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        while q:
            r, c = q.popleft()
            if (r, c) == dst:  # 도착 — BFS 라 이 값이 최단
                return dist[r][c]

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if not (0 <= nr < n and 0 <= nc < m):  # 맵 밖
                    continue
                if maps[nr][nc] == "X" or dist[nr][nc] != -1:  # 벽 / 이미 방문
                    continue
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

        return -1  # 다 가봤는데 목표에 못 닿음

    d1 = bfs(start, lever)
    if d1 == -1:
        return -1

    d2 = bfs(lever, goal)
    if d2 == -1:
        return -1

    return d1 + d2


if __name__ == "__main__":
    # S 시작 / L 레버 / E 출구 / O 길 / X 벽
    # 최소 '이동 횟수', 불가능하면 -1
    cases = [
        (["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"], 16),
        (["LOOXS", "OOOOX", "OOOOO", "OOOOO", "OOOOE"], -1),  # 시작이 갇힘
        (["SLE"], 2),  # 한 줄 — 칸 수가 아니라 이동 횟수
        (["SXL", "OOO", "EXX"], 8),  # 우회
        (["SOL", "XXX", "EOO"], -1),  # 레버는 닿지만 출구로 못 감
    ]
    for maps, expected in cases:
        assert solution(maps) == expected, ("solution", maps, expected)
        assert solution_ref(maps) == expected, ("solution_ref", maps, expected)
    print("모든 케이스 통과 (본 풀이 + 참고 정답)")
