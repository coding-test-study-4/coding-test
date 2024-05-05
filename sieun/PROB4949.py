import sys


def check_right_sentences(sentence):
    brackets_stack = []

    for value in sentence:
        if value == "(":
            brackets_stack.append(value)

        elif value == ")":
            if len(brackets_stack) == 0:
                brackets_stack.append(value)
                break

            elif brackets_stack:
                if brackets_stack[-1] != "(":
                    break

                elif brackets_stack[-1] == "(":
                    brackets_stack.pop()

        elif value == "[":
            brackets_stack.append(value)

        elif value == "]":
            if len(brackets_stack) == 0:
                brackets_stack.append(value)
                break

            elif brackets_stack:
                if brackets_stack[-1] != "[":
                    break

                elif brackets_stack[-1] == "[":
                    brackets_stack.pop()

    if len(brackets_stack) != 0:
        print("no")
    else:
        print("yes")


while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break
    else:
        check_right_sentences(list(sentence))
