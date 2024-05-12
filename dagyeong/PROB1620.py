import sys

N, M = map(int, sys.stdin.readline().split())
pokemon_dic = {}
pokemon_dic2 = {}
for idx in range(1, N+1):
    s = sys.stdin.readline().strip()
    pokemon_dic[str(idx)] = s
    pokemon_dic2[s] = idx

for _ in range(M):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        res = pokemon_dic.get(question)
    else:
        res = pokemon_dic2.get(question)
    print(res)