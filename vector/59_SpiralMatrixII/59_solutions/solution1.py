def SquareMatrix(n):
    total = n*n
    # 构建矩阵
    result = [[0]*n for _ in range(n)]
    flag_matrix = [[0]*n for _ in range(n)]

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction_index = 0

    column, row = 0, 0

    for step in range(total):
        # 结果赋值
        result[column][row] = step+1
        flag_matrix[column][row] = 1
        next_column = column + directions[direction_index][0]
        next_row = row + directions[direction_index][1]

        if (not 0 <= next_column < n) or (not 0 <= next_row < n) \
            or flag_matrix[next_column][next_row] == 1:
            direction_index = (direction_index+1)%4
        
        column += directions[direction_index][0]
        row += directions[direction_index][1]

    return result

def SquareMatrix_v2(n):
    if n == 0:
        return []

    result = [[0]*n for _ in range(n)]
    left, top = 0, 0
    right, bottom = n-1, n-1

    count = 1

    while left<=right and top <= bottom:
        # 从左往右遍历，包括左上边界和右上边界
        for i in range(left, right+1):
            result[top][i] = count
            count += 1
        # 从上往下遍历，包括右下边界
        for j in range(top+1, bottom+1):
            result[j][right] = count
            count += 1
        # 如果left==right或top==bottom则不需要再执行
        if left != right and top != bottom:
            # 从right-1开始，因为右下边界已经过，这里不经过左下边界
            for k in range(right-1, left, -1):
                result[bottom][k] = count
                count += 1
            # 包括左下边界，不包括左上边界
            for l in range(bottom, top, -1):
                result[l][left] = count
                count += 1
        left += 1
        top += 1
        right -= 1
        bottom -= 1
    return result

print(SquareMatrix_v2(3))