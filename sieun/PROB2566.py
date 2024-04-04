numbers = []
max_number = 0
column_index = 0
row_index = 0

for i in range(9):
    temp_list = list(map(int, input().split()))
    numbers.append(temp_list)

for i in range(9):
    for j in range(9):
        if numbers[i][j] > max_number:
            max_number = numbers[i][j]
            column_index = j
            row_index = i

print(max_number)
print(row_index + 1, column_index + 1, end=" ")


