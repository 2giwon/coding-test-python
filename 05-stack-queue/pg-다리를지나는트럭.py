# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 핵심: 다리를 (트럭, 위치) 쌍의 deque로 시뮬레이션. 매초 — 시간+1 → (무게 여유 시)
#       진입(loc=0) → 전체 +1칸 → 맨 앞이 loc >= 길이면 퇴장. time 선증가 + '>=' 퇴장의
#       자체 타이밍 모델 (표준은 이동→퇴장→진입 순).
# 리뷰: 1차(09/05) 25분 초과, 버그 3개 — ①빈 대기열 [0] 크래시 ②경계값 `<`→`<=` ③타이밍 밀림.
#       [재풀이 09/07 완료: 17분 40초 자력 통과 — 버그 3개 전부 처음부터 회피, 불필요한
#       칸수 체크도 스스로 제거. 남은 습관: 가드는 for 앞이 아니라 인덱스 접근([0]) 앞에]
from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_queue = deque(truck_weights)
    bridge = deque()

    time = 0
    while True:
        time += 1
        if not truck_queue and not bridge:
            break

        weight_sum = sum(w for w, _ in bridge)
        if truck_queue and weight_sum + truck_queue[0] <= weight:
            t = truck_queue.popleft()
            bridge.append((t, 0))

        for i in range(len(bridge)):
            t, loc = bridge[i]
            bridge[i] = (t, loc + 1)

        if bridge and bridge[0][1] >= bridge_length:
            bridge.popleft()

    return time


# 참고 정답: 다리를 "길이만큼 0으로 채운 큐"로 표현 — 매초 맨 앞 칸을 popleft하고
# 트럭 또는 0(빈 칸)을 append하면 이동·퇴장이 큐 연산 하나로 끝난다.
# 무게는 sum() 재계산 대신 누적 변수(on_bridge)로 O(1) 갱신.
# 마지막 트럭이 "올라간" 시점까지만 돌리고, 마저 건너는 시간은 + bridge_length로 계산.
def solution_ref(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)  # 다리의 칸들 (0 = 빈 칸)
    on_bridge = 0
    time = 0
    while trucks:
        time += 1
        on_bridge -= bridge.popleft()  # 맨 앞 칸이 빠져나감
        if on_bridge + trucks[0] <= weight:
            t = trucks.popleft()
            bridge.append(t)
            on_bridge += t
        else:
            bridge.append(0)  # 못 올라가면 빈 칸이 흘러감
    return time + bridge_length  # 마지막 트럭이 다리를 마저 건너는 시간


if __name__ == "__main__":
    cases = [
        ((2, 10, [7, 4, 5, 6]), 8),
        ((100, 100, [10]), 101),  # 트럭 1대: 진입 1초 + 건너기 100칸
        ((100, 100, [10] * 10), 110),  # 전부 동시에 올라갈 수 있는 무게 (경계값)
    ]
    for (bl, w, tw), expected in cases:
        assert solution(bl, w, list(tw)) == expected
        assert solution_ref(bl, w, list(tw)) == expected
    print("모든 케이스 통과 (재풀이 + 참고 정답)")
