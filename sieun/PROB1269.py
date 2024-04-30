def find_relative_complement_numbers(current_set):
    if current_set == "A":
        for number in A_numbers:
            if not B_numbers.__contains__(number):
                relative_complement_numbers.add(number)
    elif current_set == "B":
        for number in B_numbers:
            if not A_numbers.__contains__(number):
                relative_complement_numbers.add(number)


A, B = map(int, input().split())
A_numbers = set(list(map(int, input().split())))
B_numbers = set(list(map(int, input().split())))
relative_complement_numbers = set()

find_relative_complement_numbers("A")
find_relative_complement_numbers("B")
print(len(relative_complement_numbers))

