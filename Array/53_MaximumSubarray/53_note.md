# Question: Maximum Subarray
#### Level: median
<br>

## Question Description
Given an integer array `nums` , find the subarray with the largest `sum` , and return its `sum` .

## Example
```
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```
```
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```
```
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```
## Constraints
* 1 <= nums.length <= 10^5
* -10^4 <= nums[i] <= 10^4
## 解决思路
### 初始想法
从第一个元素开始，双层循环遍历，计算sum值并进行比较。最终返回结果最大值。
### 动态规划
计算以第i个元素结尾的连续子序列的最大sum值f(i)。可知该值为max(f(i-1)+nums[i],nums[i])。因此可通过一次遍历比较。

## 代码(Python)
```Python
初始想法 （时间超限）

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tempsum = None
        for i in range(len(nums)):
            tsum = nums[i]
            if tempsum == None or tsum > tempsum:
                tempsum = tsum
            for j in range(i+1,len(nums)):
                tsum += nums[j]
                if  tsum > tempsum:
                    tempsum = tsum
        return tempsum
```

```Python
动态规划 （执行用时112ms，占用空间26MB）

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tempsum = nums[0]
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < prev + nums[i]:
                prev = prev + nums[i]
            else:
                prev = nums[i]
            if prev > tempsum:
                tempsum = prev 
        return tempsum
```
