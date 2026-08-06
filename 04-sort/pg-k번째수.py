# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42748
# 핵심: 문제 그대로 — 자르고(i-1:j) 정렬하고(sorted) k-1번째. 1-based → 0-based 변환만 주의
#       (슬라이스 끝은 exclusive라 j 그대로). sorted()로 원본 비파괴 — 매 command가 원본 기준.
# 리뷰: 자력 통과(08/06, 정렬 1/3). 파이썬다운 형태:
#       return [sorted(array[i-1:j])[k-1] for i, j, k in commands] — 언패킹+컴프리헨션.


def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0] - 1
        j = command[1]
        k = command[2] - 1

        subArray = sorted(array[i:j])
        answer.append(subArray[k])

    return answer


if __name__ == "__main__":
    assert solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3]
    print("all passed")
