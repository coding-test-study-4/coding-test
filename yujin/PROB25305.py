#커트라인
N, k = map(int, input().split())
score_lst = list(map(int, input().split()))

score_lst.sort()

print(score_lst[N-k])