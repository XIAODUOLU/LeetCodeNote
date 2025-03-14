from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        length = len(nums)
        temp_index_value = nums[0]
        for index in range(length-2):
            if index != 0 and temp_index_value == nums[index]:
                continue
            temp_index_value = nums[index]
            left_pointer = index + 1
            right_pointer = length - 1

            while (left_pointer < right_pointer):

                temp_left_value = nums[left_pointer]
                temp_right_value = nums[right_pointer]

                if temp_index_value + temp_left_value + temp_right_value == 0:
                    result.append([temp_index_value, temp_left_value, temp_right_value])
                    while (nums[right_pointer] == temp_right_value and left_pointer < right_pointer):
                        right_pointer -= 1
                    while (nums[left_pointer] == temp_left_value and left_pointer < right_pointer):
                        left_pointer += 1
                # >0 说明需要调小总值
                elif temp_index_value + temp_left_value + temp_right_value > 0:
                    while (nums[right_pointer] == temp_right_value and left_pointer < right_pointer):
                        right_pointer -= 1
                elif temp_index_value + temp_left_value + temp_right_value < 0:
                    while (nums[left_pointer] == temp_left_value and left_pointer < right_pointer):
                        left_pointer += 1

        return result


# nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
solution = Solution()
print(solution.threeSum(nums))
