# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 핵심: 하루씩 시뮬레이션 — 매일 진도 증가 후 앞에서부터 100 이상을 popleft,
#       그날 빠진 개수를 세서 answer.append (배포 회차 = 날짜가 아니다)
# 리뷰: answer 인덱스 매칭(며칠째=인덱스)으로 접근하다 막힘 → 배치 카운트로 전환.
#       속도 deque(s)를 만들고 정작 speeds[i]를 참조한 짝 어긋남 실수.
#       대안 풀이: 완성 소요일을 math.ceil로 미리 계산 후 그룹핑 (시뮬레이션 불필요) [재풀이: 09/07]
from collections import deque


def solution(progresses, speeds):
    answer = []
    q = deque(progresses)
    s = deque(speeds)

    release_count = 0
    while q:
        for i in range(len(q)):
            q[i] += s[i]

        while q and q[0] >= 100:
            q.popleft()
            s.popleft()
            release_count += 1

        if release_count > 0:
            answer.append(release_count)
            release_count = 0

    return answer


if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
