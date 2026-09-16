# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/159993
# 핵심: 레버 필수 → 답 = (S→L 최단 이동) + (L→E 최단 이동). 하나라도 못 가면 -1.
#       "통로를 여러 번 지날 수 있다"는 조건이 두 구간을 독립적으로 풀어 더하는 것을 정당화한다.
#       BFS를 함수로 빼면 방문 표가 호출마다 새로 생겨 구간 분리가 공짜로 따라온다.
#       미방문은 -1 (이 문제는 "칸 수"가 아니라 "이동 횟수"라 출발점이 0이므로).
# 리뷰: [1차 09/10] 25분 초과 + 힌트 4단계(구조만) 후 완성. 막혔던 4가지 =
#       ①S/L/E 좌표 찾기 ②BFS 함수화 ③두 구간 더하기 ④방문 표를 새로 만들기.
#       [2차 09/16] 19분 자력 통과. 백지에서 다시 작성했고 힌트 없이 5/5.
#       🔴 1차 때 따로 고민했던 ②와 ④가 이번엔 한 번에 나왔다 —
#          "함수로 빼면 dist가 호출마다 새로 생긴다"를 알고 짰다는 뜻.
#       🔴 목표 판정을 "이웃을 볼 때"가 아니라 "큐에서 꺼낼 때"로 두었다.
#          결과적으로 ①dist 갱신 줄 중복이 사라지고 ②시작==목표인 경우까지 정확해졌다.
#          (이 문제는 S와 L이 같을 수 없어 드러나지 않지만 구조적으로 더 맞는 형태)
#       [재풀이: 1차 파일 pg-미로탈출.py 의 solution_ref 와 비교해볼 것]
#
# ─────────────────────────────────────────────────────────────────────
# 재풀이 (1차: 2026-09-10 — 25분 초과 + 힌트 4단계 후 완성)
#
# ■ 문제 요약
#   S에서 출발해 L(레버)을 반드시 당긴 뒤 E(출구)로 나간다.
#   최소 "이동 횟수"를 구한다. 못 가면 -1.
#
#     S : 시작    L : 레버    E : 출구    O : 길    X : 벽
#
#   예: ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"] → 16
#
# ■ 한 줄 구조
#   답 = (S → L 최단 이동) + (L → E 최단 이동).  하나라도 못 가면 -1.
#
#   왜 따로 풀어서 더해도 되나?
#   문제에 "통로를 여러 번 지날 수 있다"는 조건이 있다. 두 구간이 같은 칸을 다시 써도
#   되므로 서로 간섭하지 않는다. 그래서 독립적으로 풀어 더하는 것이 정당하다.
#
# ■ 1차 때 막혔던 4가지 (구조만, 코드는 직접)
#   ① S / L / E 좌표 찾기        — 격자를 한 번 훑으며 셋을 동시에 찾는다
#   ② BFS를 함수로 빼기          — bfs(시작, 목표) 형태로
#   ③ 두 구간 결과를 더하기       — 둘 중 하나라도 -1이면 전체 -1
#   ④ 구간마다 방문 표를 새로     — ③의 전제. 아래 설명 참조
#
#   💡 ②와 ④는 사실 한 몸이다. BFS를 함수로 빼면 방문 표가 호출할 때마다 새로 생긴다.
#      S→L 에서 밟은 칸을 L→E 에서 다시 밟아야 하는데, 표를 공유하면 막힌다.
#      "함수로 빼는" 진짜 이유가 코드 정리가 아니라 여기에 있다.
#
# ■ 🔴 함정 1 — 방문 체크를 `dist > 0` 으로 하면 무한 루프
#   이 문제는 "칸 수"가 아니라 "이동 횟수"를 센다. 그래서 출발점이 0이다.
#   `dist > 0` 으로 방문을 판정하면 출발점이 "아직 안 갔다"로 보여 계속 다시 들어간다.
#   (1차 시도에서 시간 초과가 난 원인)
#
#     → 미방문을 -1 로 두고 `if dist[nr][nc] > -1: continue` 로 체크한다.
#
#   ※ 게임맵 최단거리는 "칸 수"라 출발점이 1이었고, 그래서 `dist > 0` 이 통했다.
#     문제가 무엇을 세는지에 따라 미방문 표시값이 달라진다.
#
# ■ 🔴 함정 2 — `break` 는 가장 안쪽 루프 하나만 빠져나온다
#   목표에 도착했을 때 while 까지 끝내려면 `return` 이 필요하다.
#   좌표를 찾는 이중 for 에서도 같은 혼동이 있었다.
#
# ■ 막히면
#   pg-게임맵최단거리.py 의 BFS 뼈대를 먼저 보세요. 거기에 ①좌표 찾기 ②함수화
#   ③두 번 호출만 얹으면 이 문제가 됩니다.
#   1차 풀이(pg-미로탈출.py)는 마지막에 비교용으로만 열어보세요.
#
# ⏱ 목표 20분
# ─────────────────────────────────────────────────────────────────────
from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    # ① S / L / E 좌표 찾기
    start = lever = out = None
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)
            elif maps[i][j] == "E":
                out = (i, j)

    # ② BFS를 함수로 — bfs(시작좌표, 목표문자) → 이동 횟수 (못 가면 -1)
    def bfs(start, end):
        dist = [[-1 for _ in range(m)] for _ in range(n)]
        visited_queue = deque([start])

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        start_r, start_c = start
        dist[start_r][start_c] = 0
        end_r, end_c = end
        while visited_queue:
            r, c = visited_queue.popleft()

            if r == end_r and c == end_c:
                return dist[r][c]

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                if maps[nr][nc] == "X" or dist[nr][nc] > -1:
                    continue

                dist[nr][nc] = dist[r][c] + 1
                visited_queue.append((nr, nc))
        return -1

    # ③ (S→L) + (L→E), 하나라도 -1이면 -1
    lever_count = bfs(start, lever)
    out_count = bfs(lever, out)
    return -1 if lever_count < 0 or out_count < 0 else lever_count + out_count


if __name__ == "__main__":
    # S 시작 / L 레버 / E 출구 / O 길 / X 벽
    # 최소 '이동 횟수', 불가능하면 -1
    cases = [
        (["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"], 16),  # 공식 예제
        (["LOOXS", "OOOOX", "OOOOO", "OOOOO", "OOOOE"], -1),  # 시작이 갇힘
        (["SLE"], 2),  # 🔴 한 줄 — 칸 수가 아니라 이동 횟수
        (["SXL", "OOO", "EXX"], 8),  # 우회
        (["SOL", "XXX", "EOO"], -1),  # 레버는 닿지만 출구로 못 감
    ]
    for maps, expected in cases:
        assert solution(maps) == expected, (maps, expected)
    print("모든 케이스 통과")
