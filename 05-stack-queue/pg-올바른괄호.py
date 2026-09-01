# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 핵심: 여는 괄호 push, 닫는 괄호 pop — 빈 스택에서 pop 시도(닫는 게 먼저) 또는
#       순회 후 스택 잔여(안 닫힘)면 False. 한 종류 괄호라 카운터 O(1) 공간으로도 가능


def solution(s):
    stack = []

    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if stack:
                stack.pop()
            else:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(solution("()()"))  # True
    print(solution("(())()"))  # True
    print(solution(")()("))  # False
    print(solution("(()("))  # False
    print(solution(")"))  # False — 첫 글자부터 닫는 괄호
    print(solution("("))  # False — 닫히지 않고 끝남
