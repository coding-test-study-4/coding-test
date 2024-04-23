import sys

N, M = sys.stdin.readline().split()
# print(N)
# print(M)

name_dic = dict()
number_dic = dict()

for i in range(int(N)):
    name = sys.stdin.readline().strip()
    name_dic[name] = i + 1
    number_dic[int(i + 1)] = name

for i in range(int(M)):
    input_value = sys.stdin.readline().strip()

    if input_value.isdigit():
        print(number_dic[int(input_value)])
    else:
        print(name_dic[input_value])



