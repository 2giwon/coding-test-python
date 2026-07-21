# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 핵심: 세 각도로 풀 수 있음.
#   ① 전체 생성(product)+정렬: 사전 전체가 3905개(5+25+...+5^5)뿐 → 통째로 만들고 index+1.
#      파이썬 문자열 정렬 = 사전 순(짧은 접두사 우선) + A<E<I<O<U 아스키 순 → 커스텀 키 불필요.
#   ② 재귀(DFS): "가변 깊이 중첩 루프 = 재귀". preorder라 정렬 없이도 사전 순으로 생성됨.
#   ③ 가중치: 각 자리가 대표하는 서브트리 크기 = [781,156,31,6,1] (점화식: 앞×5+1).
#      순번 = Σ(모음인덱스 × 자리가중치) + 단어길이. 전체 생성 없이 O(len) 계산 — 실전 최적화.
# 리뷰: 가중치로 접근하다 막힘 → product/정렬로 1차 통과. [재풀이: 07/21] 심화로 재도전:
#   ①② 자력 재현 통과. 다만 product는 손이 기억 못 해 살짝 봄 → 근본은 재귀(별도 학습 필수).
#   ③ 가중치 점화식(앞×5+1) 자력 유도 성공.
#   교훈: "계산 가능한 규모면 나열하라"(①) vs "규모 크면 수식으로 건너뛰라"(③) — 둘 다 무기.
#         가변 깊이 완전탐색의 근본은 재귀(notes/recursion.md). [재재풀이: 07/28 — 재귀로]
from itertools import product


def solution(word):
    """① product로 전체 생성 후 정렬 → index."""
    alpha = ["A", "E", "I", "O", "U"]
    dic = []
    for c in range(1, len(alpha) + 1):
        for p in product(alpha, repeat=c):
            dic.append("".join(p))
    dic = sorted(dic)
    return dic.index(word) + 1


def newSolution(word):
    """② 재귀(DFS)로 전체 생성. preorder라 정렬 불필요."""
    dic = []

    def dfs(current):
        if len(current) > 5:
            return
        if current:
            dic.append(current)
        for ch in "AEIOU":
            dfs(current + ch)

    dfs("")
    return dic.index(word) + 1


def newSolution2(word):
    """③ 가중치: 전체 생성 없이 O(len)으로 순번 계산."""
    wordValues = [781, 156, 31, 6, 1]  # 자리별 서브트리 크기 (앞×5+1)
    answer = 0
    for i, ch in enumerate(word):
        answer += wordValues[i] * "AEIOU".index(ch)  # 모음 인덱스(A=0..U=4)
    answer += len(word)  # 각 자리의 자기 자신 몫
    return answer


if __name__ == "__main__":
    cases = {"A": 1, "AAAAA": 5, "AAAAE": 6, "AAAE": 10, "I": 1563, "EIO": 1189}
    for fn in (solution, newSolution, newSolution2):
        for word, expected in cases.items():
            assert fn(word) == expected, f"{fn.__name__}({word})={fn(word)} != {expected}"
    print("all passed")
