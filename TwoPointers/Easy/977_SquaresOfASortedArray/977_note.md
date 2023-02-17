# Question: Squares of a Sorted Array
#### Level: easy
<br>

## Question Description

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


## Example
```
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```
```
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

## Constraints

* 1 <= nums.length <= 10^4
* -10^4 <= nums[i] <= 10^4
* nums is sorted in non-decreasing order

## 解决思路

和双指针一样，但负数列表从尾部开始建立指针。结束后从尾部开始输出。


## 代码(Python)
```Python 
双指针
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neglist = []
        poslist = []
        sortedlist = []
        for i in range(len(nums)):
            if nums[i] < 0:
                neglist.append(nums[i]*nums[i])
            else:
                poslist.append(nums[i]*nums[i])
        j,k = 0,len(neglist)-1
        while True:
            if j == len(poslist):
                for h in range(len(neglist[0:k+1])-1,-1,-1):
                    sortedlist.append(neglist[h])
                break
            elif k == -1:
                for l in poslist[j:]:
                    sortedlist.append(l)
                break
            elif neglist[k] <= poslist[j]:
                sortedlist.append(neglist[k])
                k -= 1      
            elif neglist[k] > poslist[j]:
                sortedlist.append(poslist[j])
                j += 1
        return sortedlist
```