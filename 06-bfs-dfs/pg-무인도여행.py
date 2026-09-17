# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/154540
# 핵심: "최단"이 아니라 "연결된 덩어리의 크기" → BFS/DFS 둘 다 가능. 시작점이 주어지지 않으므로
#       격자를 훑으며 미방문 육지를 만날 때마다 BFS를 한 번씩 돌려 섬 하나를 통째로 소진한다.
#       🔴 visited(여기선 dist)는 함수 밖에서 "하나를 공유" — 미로 탈출(구간마다 새로 생성)과 반대.
#       공유하지 않으면 이미 센 섬을 다시 세게 된다.
# 리뷰: 25분 자력 통과 (힌트 없음). 격자가 문자열 배열이라 maps[r][c]는 문자 → int() 변환 필요.
#       개선 여지 3가지(solution_ref 반영) —
#       ① dist라는 이름이 역할과 불일치. 거리를 쓰지 않고 방문 표시만 하므로 visited가 정확
#       ② `if int(maps[nr][nc]) > 0` 은 항상 참 (육지는 1~9).
#          조건문이 있으면 읽는 사람이 "0인 경우가 있나?" 하고 멈추게 된다
#       ③ 시작 칸 식량을 bfs 진입부에서, 나머지는 루프에서 더해 처리가 두 군데로 갈림
#          → "꺼낼 때 더한다"로 바꾸면 시작점 특수 처리가 사라진다
#       [재풀이 완료: 09/17 — 18분 자력 통과. 결과는 pg-무인도여행-재풀이.py 참조]
from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    dist = [[-1 for _ in range(m)] for _ in range(n)]

    answer = []

    def bfs(src):
        sr, sc = src
        dist[sr][sc] = 0
        food = int(maps[sr][sc])

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        visited_queue = deque([src])

        while visited_queue:
            r, c = visited_queue.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                if maps[nr][nc] == "X" or dist[nr][nc] > -1:
                    continue
                if int(maps[nr][nc]) > 0:
                    food += int(maps[nr][nc])

                dist[nr][nc] = 0
                visited_queue.append((nr, nc))

        return food

    for i in range(n):
        for j in range(m):
            if maps[i][j] == "X":
                continue
            if dist[i][j] == -1:
                a = bfs((i, j))
                answer.append(a)

    return [-1] if len(answer) <= 0 else sorted(answer)


# 참고 정답: 위와 논리는 같고 세 가지가 다르다.
#   (1) 이름을 visited 로 — 거리를 쓰지 않으므로 True/False 면 충분하다
#   (2) 항상 참인 `> 0` 조건 제거 (육지는 1~9)
#   (3) 식량을 "큐에서 꺼낼 때" 더한다 → 시작 칸 특수 처리가 사라지고 합산이 한 군데로 모인다
def solution_ref(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    def bfs(sr, sc):
        visited[sr][sc] = True
        q = deque([(sr, sc)])
        food = 0

        while q:
            r, c = q.popleft()
            food += int(maps[r][c])  # 꺼낼 때 더한다 — 시작 칸도 여기서 처리됨

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if not (0 <= nr < n and 0 <= nc < m):  # 격자 밖
                    continue
                if maps[nr][nc] == "X" or visited[nr][nc]:  # 바다 / 이미 방문
                    continue
                visited[nr][nc] = True  # 큐에 넣는 순간 방문 표시 (중복 진입 방지)
                q.append((nr, nc))

        return food

    answer = []
    for r in range(n):
        for c in range(m):
            if maps[r][c] != "X" and not visited[r][c]:
                answer.append(bfs(r, c))

    return sorted(answer) if answer else [-1]


if __name__ == "__main__":
    cases = [
        (["X591X", "X1X5X", "X231X", "1XXX1"], [1, 1, 27]),
        (["XXX", "XXX", "XXX"], [-1]),  # 섬이 하나도 없음
        (["1"], [1]),  # 칸 1개짜리 섬
        (["X1X", "1X1", "X1X"], [1, 1, 1, 1]),  # 대각선은 연결이 아니다 — 섬 4개
        (["999", "9X9", "999"], [72]),  # 도넛 모양 한 덩어리 (9×8 = 72)
        (["X1X", "XXX", "X1X"], [1, 1]),  # 세로로 분리된 섬 2개
        (["12", "34"], [10]),  # 전부 육지 한 덩어리
    ]
    for maps, expected in cases:
        assert solution(maps) == expected, ("solution", maps, expected)
        assert solution_ref(maps) == expected, ("solution_ref", maps, expected)
    print("모든 케이스 통과 (본 풀이 + 참고 정답)")
