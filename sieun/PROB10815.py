N = int(input())
cards_owned = set(list(map(int, input().split())))

M = int(input())
cards_set = list(map(int, input().split()))

for card in cards_set:
    if card in cards_owned:
        print(1, end=" ")
    else:
        print(0, end=" ")
