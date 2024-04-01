#다이얼
lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = input()
T = 0

for s in S:
    for index, value in enumerate(lst):
        if s in value:
            T+=index+3

print(T)