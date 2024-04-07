#최댓값
lst = [list(map(int, input().split())) for _ in range(9)]

m_num = 0
m_row, m_col = 0, 0

for i in range(9):
    for j in range(9):
        if m_num <= lst[i][j]:
            m_num = lst[i][j]
            m_row = i + 1
            m_col = j + 1

print(m_num)
print(m_row, m_col)