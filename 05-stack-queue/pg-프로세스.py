# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 핵심: 큐가 회전해도 대상을 안 잃으려면 값만 넣지 말고 (원래 인덱스, 우선순위) 쌍을
#       enumerate로 운반한다 — "관련 값은 쌍으로 묶어 이동" (기능개발 짝 어긋남의 예방책).
#       꺼낸 우선순위보다 높은 게 큐에 남아있으면 뒤로, 없으면 실행 카운트+1.
# 리뷰: location 추적 방법에서 막힘(25분 초과, 힌트 2단계 사용) → enumerate 쌍으로 해결.
#       빈 큐 특수 처리(maxp=p)는 any() 판정으로 바꾸면 통째로 불필요. [재풀이: 09/03]
from collections import deque


def solution(priorities, location):
    pqueue = deque(enumerate(priorities))

    pop_count = 0
    while pqueue:
        idx, pr = pqueue.popleft()
        if pqueue:
            max_pr = max(other for _, other in pqueue)
        else:
            max_pr = pr

        if pr < max_pr:
            pqueue.append((idx, pr))
        else:
            pop_count += 1
            if idx == location:
                return pop_count

    return pop_count


# 참고 정답: any()로 "나보다 높은 게 하나라도 있나"만 판정 — 단락 평가로 평균 더 빠르고,
# 빈 큐면 False라 특수 처리 자체가 사라진다
def solution_ref(priorities, location):
    q = deque(enumerate(priorities))
    order = 0
    while q:
        idx, pr = q.popleft()
        if any(pr < other for _, other in q):
            q.append((idx, pr))
        else:
            order += 1
            if idx == location:
                return order
    return order


if __name__ == "__main__":
    cases = [
        (([2, 1, 3, 2], 2), 1),  # 우선순위 3이 가장 먼저 실행
        (([1, 1, 9, 1, 1, 1], 0), 5),
        (([1], 0), 1),  # 프로세스 1개
        (([3, 3, 3], 1), 2),  # 전부 같은 우선순위면 들어온 순서대로
    ]
    for (priorities, location), expected in cases:
        assert solution(priorities, location) == expected
        assert solution_ref(priorities, location) == expected
    print("모든 케이스 통과 (본 풀이 + 참고 정답)")
