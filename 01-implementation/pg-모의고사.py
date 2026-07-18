# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 핵심: 패턴별 순환 매칭으로 채점(i % len) → 최고점 집계 → 동점자 수집 (2-pass)
# 리뷰: 1차 - 1등 기준을 고정 앵커(1번 학생)와 비교해 오답 / 2차 - one-pass 명단 갱신 중
#       ranks[rankIndex] 교차 인덱스 대입으로 IndexError (반례 [3,3,2]).
#       교훈: ① 최댓값 기준 선발은 "집계 먼저, 수집은 2-pass"
#            ② 불안한 분기는 그 분기를 때리는 입력으로 제출 전 로컬 확인 (30초 룰)
#       [재풀이 07/18 성공 — 안 보고 재현(newSolution), 제출 통과. 채점(enumerate)과
#        2-pass(집계 먼저) 모두 자력 재현, 과거 오답 반례 4개 전부 통과. 디버그 print 없음 ✅]
def solution(answers):
    # 세 수포자의 찍기 패턴을 하나의 리스트로 묶는다 (코드 3벌 복사 방지)
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]

    # [1단계] 채점: 수포자마다 몇 개 맞혔는지 센다
    scores = []
    for pattern in patterns:
        score = 0
        for i, answer in enumerate(answers):  # i = 문제 번호(0부터)
            if pattern[i % len(pattern)] == answer:  # 패턴은 반복되니까 % 로 순환
                score += 1
        scores.append(score)

    # [2단계] 최고점이 몇 점인지 확정 (집계 먼저!)
    best = max(scores)

    # [3단계] 최고점과 같은 사람만 골라 담는다 (기준이 확정됐으니 안 틀림)
    ranks = []
    for i, score in enumerate(scores):
        if score == best:
            ranks.append(i + 1)  # 수포자 번호는 1부터라 +1

    return ranks


def newSolution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    counts = [0, 0, 0]

    for idx, answer in enumerate(answers):
        if answer == first[idx % len(first)]:
            counts[0] += 1
        if answer == second[idx % len(second)]:
            counts[1] += 1
        if answer == third[idx % len(third)]:
            counts[2] += 1

    maxCount = max(counts)
    ranks = []
    for idx, count in enumerate(counts):
        if maxCount == count:
            ranks.append(idx + 1)

    return ranks


if __name__ == "__main__":
    # 로컬 검증용 테스트 케이스 (오답 반례 포함)
    print(solution([1, 2, 3, 4, 5]))  # [1]
    print(solution([1, 3, 2, 4, 2]))  # [1, 2, 3]
    print(solution([2, 2, 2]))  # [2]      ← 1차 오답 반례
    print(solution([3, 3, 2]))  # [3]      ← 2차 IndexError 반례
