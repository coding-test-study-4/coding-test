import sys
readline = sys.stdin.readline

v_max, v_argmax = -1, (-1, -1)
for i in range(9):
    for j, v in enumerate(map(int, readline().split(' '))):
        if v_max < v:   v_max, v_argmax = v, (i, j)

print(v_max)
print(f"{v_argmax[0]+1} {v_argmax[1]+1}")