# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 핵심: 사전 전체가 3905개(5+25+...+5^5)뿐 → 순번을 계산하지 말고 통째로 생성(product)해서
#       정렬 후 index+1. 파이썬 문자열 정렬 = 사전 순(접두사 짧은 쪽 우선) + A<E<I<O<U가
#       아스키 순이라 커스텀 키 불필요 (이 두 가지를 확인하고 쓴 것이 포인트).
# 리뷰: 가중치(자릿수 기여도) 계산으로 접근하다 막힘 → 힌트 2단계(크기 계산→통째 생성)로 전환.
#       교훈: "계산 가능한 규모면 계산하지 말고 나열하라" — 크기부터 세는 습관.
#       [재풀이: 07/21 — 심화 도전: 가중치(각 자리 781/156/31/6/1) 방식으로 다시 풀기]
# 나의 생각
# 각 자릿 수에 대한 가중치
# 각 알파벳의 pos 값을 더해서
# 전달해준 word를 하나의 char 별로 확인해서
# 가중치 + 알파벳 pos로 결과를 더하여 리턴
from itertools import product


def solution(word):
    alpha = ["A", "E", "I", "O", "U"]

    dic = []  # ruff C408: list() 대신 리터럴
    for c in range(1, len(alpha) + 1):
        for p in product(alpha, repeat=c):
            dic.append("".join(p))

    dic = sorted(dic)

    return dic.index(word) + 1


if __name__ == "__main__":
    print(solution("AAAAE"))
    print(solution("AAAE"))
    print(solution("I"))
    print(solution("EIO"))
