import sys


def check_right_sentence(brackets):
    bracket_stack = []

    for bracket in brackets:
        if bracket == "(":
            bracket_stack.append(bracket)

        elif bracket == ")":
            if len(bracket_stack) == 0:
                bracket_stack.append(bracket)
                break

            elif bracket_stack:
                bracket_stack.pop()

    if len(bracket_stack) != 0:
        print("NO")
    else:
        print("YES")


T = int(sys.stdin.readline())

for _ in range(T):
    brackets = list(sys.stdin.readline())
    # print(brackets)
    if brackets[0] == ")":
        print("NO")
    else:
        check_right_sentence(brackets)
