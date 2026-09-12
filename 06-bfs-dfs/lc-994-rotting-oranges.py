# 문제: https://leetcode.com/problems/rotting-oranges/
# 핵심: 다중 시작점 BFS — 썩은 오렌지(2)를 "전부" 처음에 큐에 넣고 한 번만 돌린다.
#       하나씩 따로 돌리면 겹치는 영역을 중복 계산한다. 시작점을 다 넣어두면
#       큐가 알아서 동시에 퍼뜨린다(거리 0인 칸들 → 1인 칸들 → 2인 칸들 …).
#       🔴 "도달 못 함(-1)" 판정은 BFS 결과가 아니라 밖에서 한다 —
#       BFS는 닿는 칸만 방문하므로 고립된 오렌지는 탐색에 아예 나타나지 않는다.
#       그래서 신선한 개수(fresh)를 미리 세고, 썩힐 때마다 하나씩 줄여 마지막에 남았는지로 판정.
# 리뷰: 25분 초과. BFS 골격은 처음부터 맞았고 막힌 건 전부 "판정" 부분이었다 —
#       ① "마지막에 썩힌 칸"을 답으로 삼음 → 같은 층에 여러 칸이 있으면 최댓값 보장 없음. max로
#       ② -1을 BFS 결과로 판정하려 함 → 고립 칸은 방문 자체가 안 되니 fresh 카운터로 판정해야 함
#       ③ 방문 체크를 `dist > 0`으로 → 시작 칸 dist가 0이라 미방문으로 오인 (게임맵과 같은 함정).
#          미방문을 -1로 뒀으면 `!= -1`로 비교
#       남은 흠: 83행 `or -1`은 도달 불가 코드다(fresh==0이면 위에서 return 0, 아니면 max ≥ 1).
#       73행 `== 2` 검사도 불필요 — 썩은 칸은 dist가 0이라 위 `!= -1`에서 이미 걸린다.
#       [재풀이: 09/19 — 판정 3종을 처음부터 맞게]
from collections import deque


def orangesRotting(grid):
    n, m = len(grid), len(grid[0])
    dist = [[-1 for _ in range(m)] for _ in range(n)]
    q = deque()
    fresh = 0

    for row in range(n):
        for col in range(m):
            if grid[row][col] == 2:
                q.append((row, col))
                dist[row][col] = 0
            if grid[row][col] == 1:
                fresh += 1

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    if fresh == 0:
        return 0

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            if grid[nr][nc] == 0 or dist[nr][nc] != -1:
                continue
            if grid[nr][nc] == 2:
                continue

            dist[nr][nc] = dist[r][c] + 1
            fresh -= 1
            q.append((nr, nc))

    if fresh > 0:
        return -1

    return max(max(row) for row in dist) or -1


# 참고 정답: 층 단위(level-order) BFS — "분"을 직접 세는 방식.
# 위 풀이는 칸마다 시간을 적고 마지막에 최댓값을 구하지만, 이 방식은
# 큐에 들어있는 "이번 분의 썩은 오렌지"를 한 묶음씩 처리하고 분을 1 올린다.
#   for _ in range(len(q))  ← 지금 큐 길이만큼만 = 이번 층만 처리 (그 안에서 append된 건 다음 층)
# 시간 표(dist)가 통째로 필요 없어지고, 격자에 직접 2를 써서 방문 표시를 겸한다.
# 남은 신선한 오렌지가 0이 되면 즉시 멈추므로 불필요한 순회도 없다.
def orangesRotting_ref(grid):
    n, m = len(grid), len(grid[0])
    q = deque()
    fresh = 0

    for r in range(n):
        for c in range(m):
            if grid[r][c] == 2:
                q.append((r, c))  # 시작점 전부를 미리 넣는다
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:  # 썩힐 게 없으면 0분
        return 0

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    minutes = 0

    while q and fresh > 0:
        minutes += 1
        for _ in range(len(q)):  # 이번 분에 썩어 있던 것들만 처리
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if not (0 <= nr < n and 0 <= nc < m):  # 격자 밖
                    continue
                if grid[nr][nc] != 1:  # 빈칸이거나 이미 썩음
                    continue
                grid[nr][nc] = 2  # 격자에 직접 표시 = 방문 표시 겸용
                fresh -= 1
                q.append((nr, nc))

    return -1 if fresh > 0 else minutes


if __name__ == "__main__":
    cases = [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),  # LeetCode 예제 1
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),  # 예제 2 — 좌하단이 고립돼 못 썩음
        ([[0, 2]], 0),  # 예제 3 — 신선한 오렌지가 없음
        ([[0]], 0),  # 빈 칸만
        ([[1]], -1),  # 신선한 오렌지 1개 + 썩은 것 없음
        ([[2, 2], [2, 2]], 0),  # 전부 이미 썩음
        ([[2, 1, 1], [1, 1, 1], [1, 1, 2]], 2),  # 🔴 시작점 2개 — 하나씩 돌리면 답이 커진다
    ]
    for grid, expected in cases:
        # 각 풀이에 격자 복사본을 넘긴다 (참고 정답은 격자를 직접 수정하므로)
        assert orangesRotting([row[:] for row in grid]) == expected, ("본 풀이", grid)
        assert orangesRotting_ref([row[:] for row in grid]) == expected, ("참고 정답", grid)
    print("모든 케이스 통과 (본 풀이 + 층 단위 참고 정답)")
