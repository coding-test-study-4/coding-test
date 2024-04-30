import sys

N = int(sys.stdin.readline())
card_number_dic = dict()
card_numbers = list(map(int, input().split()))
# print(card_numbers)

for card_number in card_numbers:
    if card_number in card_number_dic:
        card_number_dic[card_number] += 1

    else:
        card_number_dic[card_number] = 1

M = int(sys.stdin.readline())
find_values = list(sys.stdin.readline().split())
# print(find_values)

for value in find_values:
    if int(value) in card_number_dic:
        print(card_number_dic[int(value)], end=" ")
    else:
        print(0, end=" ")

