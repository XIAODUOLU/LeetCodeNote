matrix = [[1,2,3],[4,5,6],[7,8,9]]

## 顺时针遍历，先定一个同样大小的数组

def sprial_matrix(matrix):
    # 空值，排除
    if not matrix or not matrix[0]:
        return []

    columns = len(matrix)
    rows = len(matrix[0])
    flag_matrix = [[0 for _ in range(rows)] for _ in range(columns)]

    # 从0开始，遍历total次
    total = columns * rows
    column, row = 0, 0

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction_index = 0

    result = []
    for _ in range(total):
        result.append(matrix[column][row])
        flag_matrix[column][row] = 1

        next_column, next_row = column + directions[direction_index][0], row + directions[direction_index][1]

        if next_column >= columns or next_column < 0 \
            or next_row >= rows or next_row < 0 or flag_matrix[next_column][next_row] == 1:
            direction_index = (direction_index + 1) % 4
        
        column += directions[direction_index][0]
        row += directions[direction_index][1]


    return result

print(sprial_matrix(matrix))
