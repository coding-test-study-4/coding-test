import sys

n = int(sys.stdin.readline().strip())
check_dic = {}
for _ in range(n):
    k, v = sys.stdin.readline().split()
    check_dic[k] = v

for k, v in sorted(check_dic.items(), reverse=True):
    if v == 'enter':
        print(k)