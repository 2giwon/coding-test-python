# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 핵심: 각 명함을 (긴 변, 짧은 변)으로 정규화 → 각각의 max
# 리뷰: 1차 오답 — 회전 판단은 조건문으로 했는데 지갑 확장 시 회전을 안 시킴
#       (반례 [[60,50],[30,70]] → 4200 ≠ 3500). 교훈: "회전 가능"이면 비교 전에
#       (긴 변, 짧은 변)으로 정규화 먼저 → 축이 독립 → 각각 max
#       [재풀이 07/18 성공 — 안 보고 재현, 제출 통과. newSolution이 재풀이 버전.
#        반복 습관 발견: 디버그 print 미청소 (카펫에 이어 2회) → 제출 전 30초 청소 룰]
def solution(sizes):
    max_long = max(max(s) for s in sizes)  # 모든 명함을 눕혔을 때 가로의 최대 = 80
    max_short = max(min(s) for s in sizes)  # 모든 명함을 눕혔을 때 세로의 최대 = 50
    return max_long * max_short  # 80 × 50 = 4000


def newSolution(sizes):
    newCards = []

    maxW = 0
    maxH = 0
    for card in sizes:
        w = max(card[0], card[1])
        h = min(card[0], card[1])

        newCards.append([w, h])

    for newCard in newCards:
        maxW = max(maxW, newCard[0])
        maxH = max(maxH, newCard[1])

    return maxW * maxH
