# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 핵심: "최단" 신호 → BFS. dist 표(0 = 미방문, visited 겸용)에 "시작에서 몇 칸째"를 적으며
#       큐로 층층이 퍼진다. 큐는 거리 1 → 2 → 3 … 순서로 흐르므로 도착 칸에 처음 적힌 값이 최단.
#       이웃 검사 3종: 맵 밖 / 벽(0) / 이미 방문(dist > 0).
# 리뷰: 30분 초과 + 힌트 3단계. 교훈 3개 —
#       ① 처음에 DFS로 접근해 30분 소진. "최단"은 BFS — 신호를 읽고 도구를 고르는 게 구현보다 먼저.
#       ② `[[0]*m]*n` 은 같은 행을 n번 가리킴 → 반드시 `[[0]*m for _ in range(n)]`.
#       ③ 행 = len(maps), 열 = len(maps[0]). x/y로 부르면 수학 좌표(x=가로)와 충돌해 뒤바뀜 →
#          r(행)/c(열)로 부를 것. 정사각 테스트만 통과하고 직사각에서 런타임 에러 났음.
#       [재풀이: 09/10 — r/c + dr/dc 표준형(solution_ref)으로 백지에서 15분 목표]
from collections import deque


def solution(maps):
    n = len(maps)  # 행 수
    m = len(maps[0])  # 열 수

    dist = [[0] * m for _ in range(n)]
    dist[0][0] = 1

    visited_queue = deque()
    visited_queue.append((0, 0))

    # 이웃 칸 하나를 검사해서 갈 수 있으면 거리 기록 + 줄 세우기.
    # cur_dist = 지금 꺼낸 칸까지의 거리. 루프 밖에 두어야 한다 —
    # 루프 안에서 정의하면 함수가 루프 변수(x, y)를 늦게 바인딩해 ruff B023 경고가 난다.
    def try_visit(nx, ny, cur_dist):
        if nx >= n or ny >= m or nx < 0 or ny < 0:
            return
        if maps[nx][ny] == 0:
            return
        if dist[nx][ny] > 0:
            return

        dist[nx][ny] = cur_dist + 1
        visited_queue.append((nx, ny))

    while visited_queue:
        (x, y) = visited_queue.popleft()  # x = 행, y = 열 (이름과 달리 x가 세로)
        cur = dist[x][y]

        try_visit(x + 1, y, cur)  # 아래 (행 +1)
        try_visit(x - 1, y, cur)  # 위   (행 -1)
        try_visit(x, y + 1, cur)  # 오른쪽 (열 +1)
        try_visit(x, y - 1, cur)  # 왼쪽   (열 -1)

    return -1 if dist[n - 1][m - 1] == 0 else dist[n - 1][m - 1]


# 참고 정답: 격자 BFS 표준형 — r(행)/c(열) 이름, 방향 배열 dr/dc + for i in range(4).
# 위 풀이와 논리는 같고 형태만 다르다. 8방향이면 dr/dc 배열만 늘리면 된다.
def solution_ref(maps):
    n, m = len(maps), len(maps[0])
    dist = [[0] * m for _ in range(n)]
    dist[0][0] = 1
    q = deque([(0, 0)])
    dr = [1, -1, 0, 0]  # 아래, 위, 오른쪽, 왼쪽 — 행의 변화량
    dc = [0, 0, 1, -1]  # 열의 변화량

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < n and 0 <= nc < m):  # 맵 밖
                continue
            if maps[nr][nc] == 0 or dist[nr][nc] > 0:  # 벽 or 이미 방문
                continue
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

    return dist[n - 1][m - 1] or -1  # 0(미도달)이면 -1


if __name__ == "__main__":
    cases = [
        (
            [
                [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [0, 0, 0, 0, 1],
            ],
            11,
        ),
        (
            [
                [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1],
            ],
            -1,  # 도착 지점이 막혀 있음
        ),
        ([[1]], 1),  # 시작 = 도착, 칸 1개
        ([[1, 1], [1, 1]], 3),  # 2×2
        ([[1, 1, 1], [1, 1, 1]], 4),  # 직사각 2행 3열 — 행/열 뒤바뀜을 잡는 케이스
        ([[1, 1], [1, 1], [1, 1]], 4),  # 직사각 3행 2열
        ([[1, 1, 0], [0, 1, 1], [1, 1, 1]], 5),  # notes/bfs-ladder.md 추적 예제
    ]
    for maps, expected in cases:
        assert solution(maps) == expected, (maps, expected)
        assert solution_ref(maps) == expected, (maps, expected)
    print("모든 케이스 통과 (본 풀이 + 표준형 참고 정답, 직사각 포함)")
