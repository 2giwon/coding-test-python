# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 핵심: 하루씩 시뮬레이션 — 매일 진도 증가 후 앞에서부터 100 이상을 popleft,
#       그날 빠진 개수를 세서 answer.append (배포 회차 = 날짜가 아니다)
# 리뷰: 1차(08/31) answer 인덱스 매칭(며칠째=인덱스)으로 접근하다 막힘 → 배치 카운트로 전환.
#       속도 deque(s)를 만들고 정작 speeds[i]를 참조한 짝 어긋남 실수.
#       [재풀이 09/07 완료: 15분 자력 통과 — 짝 어긋남을 처음부터 회피, 배치 카운트 재현.
#       남은 습관: 조건 반복은 range+break 대신 while로]
from collections import deque


def solution(progresses, speeds):
    pqueue = deque(progresses)
    squeue = deque(speeds)
    complete = []
    count = 0
    while pqueue:
        for i in range(len(pqueue)):
            pqueue[i] += squeue[i]

        while pqueue and pqueue[0] >= 100:
            pqueue.popleft()
            squeue.popleft()
            count += 1

        if count > 0:
            complete.append(count)
            count = 0

    return complete


# 참고 정답: 시뮬레이션 없이 "각 기능의 완성 소요일"을 먼저 계산 — 사건이 일어나는
# 시점만 보면 루프 한 번으로 끝난다. front = 현재 배포 그룹의 기준일(가장 늦은 앞 기능):
# 기준일 안에 끝나는 기능은 같은 배포에 묶이고, 더 오래 걸리는 기능이 새 그룹을 연다.
def solution_ref(progresses, speeds):
    import math

    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds, strict=True)]
    answer = []
    front = days[0]
    count = 0
    for d in days:
        if d <= front:
            count += 1
        else:
            answer.append(count)
            front, count = d, 1
    answer.append(count)
    return answer


if __name__ == "__main__":
    cases = [
        (([93, 30, 55], [1, 30, 5]), [2, 1]),
        (([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]), [1, 3, 2]),
        (([100], [1]), [1]),  # 이미 완성된 기능 1개
        (([30, 30], [50, 50]), [2]),  # 같은 날 동시 배포
    ]
    for (progresses, speeds), expected in cases:
        assert solution(progresses, speeds) == expected
        assert solution_ref(progresses, speeds) == expected
    print("모든 케이스 통과 (재풀이 + 참고 정답)")
