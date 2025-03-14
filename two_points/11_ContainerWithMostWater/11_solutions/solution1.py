from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # n >= 2
        right_pointer = len(height) - 1
        left_pointer = 0

        max_area = 0
        temp_height = 0
        while (left_pointer != right_pointer):
            length = right_pointer - left_pointer
            if height[left_pointer] <= height[right_pointer]:
                temp_height = height[left_pointer]
                left_pointer += 1
            else:
                temp_height = height[right_pointer]
                right_pointer -= 1

            max_area = max(max_area, length * temp_height)

        return max_area

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))



