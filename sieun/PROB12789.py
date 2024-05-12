N = int(input())
students = list(map(int, input().split()))
students_stack = []
rank = 1

for student in students:
    while students_stack and students_stack[-1] == rank:
        students_stack.pop()
        rank += 1
    if student == rank:
        rank += 1
    else:
        students_stack.append(student)

while students_stack:
    if students_stack.pop() == rank:
        rank += 1
    else:
        print("Sad")
        break
else:
    print("Nice")
