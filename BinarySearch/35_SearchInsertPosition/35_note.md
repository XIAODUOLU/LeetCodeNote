# Question: Search Insert Position
#### Level: easy
<br>

## Question Description
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

## Example
```
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
```
```
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
```
```
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
```
## Constraints
* 1 <= nums.length <= 10^4
* -10^4 <= nums[i] <= 10^4
* `nums` contains distinct values sorted in ascending order.
* -10^4 <= target <= 10^4

## 解决思路
二分查找。如果不存在于数组中，判断target是否在当前索引前后值之间。
## 代码(Python)
```Python
循环法（执行用时36ms，内存消耗15.9MB）
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                right = mid - 1
                if mid - 1 < 0 :
                    return mid
                elif nums[mid-1] < target:
                    return mid
            else:
                left = mid + 1
                if mid + 1 > len(nums)-1:
                    return mid + 1
                elif nums[mid+1] > target:
                    return mid + 1
        return -1
```