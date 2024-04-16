def solve(x, y, color):
    count = 0
    for i in range(8):
        current_color = color if i % 2 == 0 else change_color(color)
        for j in range(8):
            if graph[y + i][x + j] != current_color:
                count += 1
            current_color = change_color(current_color)
    return count


def change_color(current_color):
    return "W" if current_color == "B" else "B"


N, M = map(int, input().split())
graph = []
answer = float('inf')

for _ in range(N):
    graph.append(list(map(str, input())))

# print(graph)

for start_y in range(N - 7):
    for start_x in range(M - 7):
        repaint_black_start = solve(start_x, start_y, "B")
        repaint_white_start = solve(start_x, start_y, "W")
        answer = min(answer, repaint_black_start, repaint_white_start)

print(answer)

