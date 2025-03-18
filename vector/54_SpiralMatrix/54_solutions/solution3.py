nums = [[1,2,3],[4,5,6],[7,8,9]]

def sprial_matrix(nums):
    ## 如果nums不存在则返回空
    if not nums or not nums[0]:
        return []

    ## 创建一个flag矩阵
    columns = len(nums)
    rows = len(nums[0])
    flag_matrix = [[0]*rows for _ in range(columns)]

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    column = 0
    row = 0
    total = columns * rows

    direction_index = 0

    result = []

    for _ in range(total):
        result.append(nums[column][row])
        flag_matrix[column][row] = 1

        next_column = column + directions[direction_index][0]
        next_row = row + directions[direction_index][1]

        if (not 0 <= next_column < columns) or (not 0 <= next_row < rows) \
            or (flag_matrix[next_column][next_row] == 1):
            # 改变方向
            direction_index = (direction_index + 1) % 4

        
        column += directions[direction_index][0]
        row += directions[direction_index][1]

    return result

def sprial_matrix_v2(nums):
    ## 如果nums不存在则返回空
    if not nums or not nums[0]:
        return []
    ## 定义上左下右
    left = 0
    top = 0
    right = len(nums[0]) - 1
    bottom = len(nums) - 1

    result = []

    while left <= right and top <= bottom:
        # 从左往右遍历, 遍历right边界
        for i in range(left, right+1):
            result.append(nums[top][i])
        # 从右往下遍历，遍历bottom边界
        for j in range(top+1, bottom+1):
            result.append(nums[j][right])
        # 如果left == right或者top == bottom，就不需要再遍历了，会导致重复
        if left != right and top != bottom:
            # 排除右边界，因为在bottom里已排除，排除左边界，因为会在从下往上遍历时命中
            for k in range(right-1, left, -1):
                result.append(nums[bottom][k])
            
            for l in range(bottom, top, -1):
                result.append(nums[l][left])

        left +=1
        right -=1
        top +=1
        bottom -=1

    return result

print(sprial_matrix_v2(nums))
