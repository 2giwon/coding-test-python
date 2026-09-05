# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 핵심: 다리를 (트럭, 위치) 쌍의 deque로 시뮬레이션. 매초 — 시간+1 → (무게·칸 여유 시)
#       진입(loc=0) → 전체 +1칸 → 맨 앞이 loc >= 길이면 퇴장. 진입을 이동보다 앞에 두는
#       대신 time 선증가 + '>=' 퇴장으로 타이밍을 맞춘 자체 모델 (표준은 이동→퇴장→진입 순).
# 리뷰: 25분 초과, 버그 3개를 순서대로 잡음 — ①대기열 비었을 때 [0] 접근 크래시
#       ②경계값 `<` → `<=` (10대×10kg=100kg 딱 떨어지는 케이스가 잡아줌: 201→110)
#       ③퇴장하는 초에 새 트럭이 못 올라가는 타이밍 밀림.
#       개선 여지: 매초 sum() 재계산 O(n) → 진입/퇴장 시 누적 합 변수 갱신이면 O(1). [재풀이: 09/06]
from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_queue = deque(truck_weights)
    bridge_queue = deque()
    time = 0

    while True:
        time += 1
        if not truck_queue and not bridge_queue:
            break
        if (
            truck_queue
            and sum(elem for elem, _ in bridge_queue) + truck_queue[0] <= weight
            and bridge_length > len(bridge_queue)
        ):
            w = truck_queue.popleft()
            bridge_queue.append((w, 0))

        for i in range(len(bridge_queue)):
            truck, loc = bridge_queue[i]
            bridge_queue[i] = (truck, loc + 1)

        if bridge_queue and bridge_queue[0][1] >= bridge_length:
            bridge_queue.popleft()

    return time


if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))  # 8
    print(solution(100, 100, [10]))  # 101 — 트럭 1대: 진입 1초 + 건너기 100칸
    print(solution(100, 100, [10] * 10))  # 110 — 전부 동시에 올라갈 수 있는 무게
