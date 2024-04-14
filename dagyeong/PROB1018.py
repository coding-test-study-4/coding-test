import sys

N, M = map(int, sys.stdin.readline().split())
chess_board = [sys.stdin.readline() for _ in range(N)]
result = []

for i in range(N-7):
    for j in range(M-7):
        W_cnt = 0
        B_cnt = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:                # 첫 번 째 칸이 W, B 값 중 하나가 들어감 -> 두 가지 경우 모두 생각해야 함
                    if chess_board[x][y] != 'W':    # x, y 자리가 W자리가 아닌 경우
                        W_cnt += 1
                    if chess_board[x][y] != 'B':    # x, y 자리가 B자리가 아닌 경우
                        B_cnt += 1
                else:                               # 위의 조건문의 옆자리
                    if chess_board[x][y] != 'W':    # 위에서 'W'가 아닌 경우 W_cnt += 1 했으므로, 옆자리의 경우 반대여야 함
                        B_cnt += 1
                    if chess_board[x][y] != 'B':
                        W_cnt += 1
        result.append(W_cnt)
        result.append(B_cnt)

print(min(result))
                