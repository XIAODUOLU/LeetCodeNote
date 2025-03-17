matrix = [[1,2,3],[4,5,6],[7,8,9]]

## 顺时针遍历，先定一个同样大小的数组

def sprial_matrix(matrix):
    ## 定义left, right分别为0，len-1
    ## 定义top, bottom分别为0，len-1
    if not matrix or not matrix[0]:
        return []
    columns = len(matrix)
    rows = len(matrix[0])

    left, top = 0, 0
    right, bottom = rows-1, columns-1

    result = []

    # = 遍历边界
    while left <= right and top <= bottom:
        # 从左往右遍历
        for i in range(left, right+1):
            result.append(matrix[top][i])
        # 从右上往右下遍历
        for j in range(top+1, bottom+1):
            result.append(matrix[j][right])
        # 如果left=right，则不往回遍历，如果top=bottom也不能遍历，因为会重复
        if left < right and top < bottom:
            # 不需要left-1，因为遍历bottom~top时会加上，但需要right-1
            for h in range(right-1, left, -1):
                result.append(matrix[bottom][h])
            # 不需要top-1，因为第一次就遍历了
            for k in range(bottom, top, -1):
                result.append(matrix[k][left])
        
        left, right, top, bottom = left+1, right-1, top+1, bottom -1
    return result
