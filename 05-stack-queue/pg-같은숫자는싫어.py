# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 핵심: 마지막에 쌓은 값(스택 top)과 다를 때만 append — 연속 중복만 걸러진다


def solution(arr):
    answer = []

    for i in arr:
        if not answer or i != answer[-1]:
            answer.append(i)

    return answer


if __name__ == "__main__":
    print(solution([1, 1, 3, 3, 0, 1, 1]))  # [1, 3, 0, 1]
    print(solution([4, 4, 4, 3, 3]))  # [4, 3]
