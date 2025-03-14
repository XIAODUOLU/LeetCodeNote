from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        # 只有1个值或没有值时不用操作
        if nums_length <= 1:
            return
        
        left_pointer = 0
        right_pointer = 0
        while (right_pointer < nums_length):
            if nums[right_pointer] != 0:
                if left_pointer == right_pointer:
                    left_pointer += 1
                else:
                    # 交换
                    nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                    left_pointer += 1
            right_pointer += 1
            
nums = [0]
solution = Solution()
solution.moveZeroes(nums)
print(nums)