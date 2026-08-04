# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 핵심: 두 리스트를 정렬하면 같은 값은 같은 위치에 줄 섬 → zip으로 앞에서 비교,
#       처음 어긋나는 지점이 완주 못 한 선수. 끝까지 같으면 participant 마지막 원소.
#       (동명이인은 "개수"까지 정렬 위치로 반영되어 자동 해결) O(n log n)
# 리뷰: 첫 시도 set(completion) 차집합 → 동명이인에서 개수를 못 세 오답(정확성·효율성 동시 실패).
#       set은 "존재"만 알고 "개수"를 모름. 문제가 개수를 물으면 set은 후보가 아님.
#       교훈: ①"존재냐 개수냐" 먼저 판단 → 자료구조 결정 ②반례는 제약과 대조하고 만든다
#       [재풀이 08/04 성공 ✅ — 정렬 비교 재현 + 카운팅 버전 자력 작성(참가자를 세고 완주자를
#       깎아 "남는 1명" 반환 — 힌트와 반대 방향의 자기 발상). 두 방식 모두 자력 → 졸업]
from collections import Counter


def solution(participant, completion):
    """정렬 비교 O(n log n) — 첫 통과 버전."""
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion, strict=False):  # 길이 다름이 의도(짧은 쪽서 멈춤)
        if p != c:
            return p
    return participant[-1]


def solution_count(participant, completion):
    """카운팅 O(n) — 재풀이(08/04) 자력 버전. 참가자 개수에서 완주자를 깎으면 1명 남는다."""
    pCounter = Counter(participant)

    for c in completion:
        pCounter[c] -= 1
        if pCounter[c] == 0:
            del pCounter[c]

    return list(pCounter.keys())[0]


if __name__ == "__main__":
    marathon = (
        ["marina", "josipa", "nikola", "vinko", "filipa"],
        ["josipa", "filipa", "marina", "nikola"],
    )
    for fn in (solution, solution_count):
        # 공식 예제
        assert fn(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo"
        assert fn(list(marathon[0]), list(marathon[1])) == "vinko"
        assert fn(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) == "mislav"
        # 오답 반례 (제약과 대조하여 작성)
        assert fn(["a", "a", "b"], ["a", "a"]) == "b"  # set 함정: 완주자 동명이인
        assert fn(["mislav", "mislav", "ana"], ["mislav", "ana"]) == "mislav"  # 정답이 동명이인
        assert fn(["a", "a", "a"], ["a", "a"]) == "a"  # 전원 동명이인, 개수 감소
        assert fn(["a", "b", "c"], ["a", "b"]) == "c"  # 정답이 정렬 맨 끝
    print("all passed")
