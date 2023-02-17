# Question: Merge Sorted Array
#### Level: easy
<br>

## Question Description
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

## Example
```
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```
```
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
```
```
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
```

## Constraints
* nums1.length == m + n
* nums2.length == n
* 0 <= m, n <= 200
* 1 <= m + n <= 200
* -10^9 <= nums1[i], nums2[j] <= 10^9

## 解决思路
### 双指针

对两个列表各自建立一个指针。先比较当前指针所指元素大小，nums1中元素大于nums2中元素时将nums2中元素插入当前位置左边并后退指针。nums1中元素小于nums2中元素时后退nums1指针。这样只需一遍即可完成。

## 代码(Python)

```Python
双指针
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1temp = nums1[0:m]
        i,j,k = 0,0,0
        while True:
            if i == m:
                for h in nums2[j:]:
                    nums1[k] = h
                    k += 1
                break
            elif j == n:
                for l in nums1temp[i:]:
                    nums1[k] = l
                    k += 1
                break
            elif nums1temp[i] <= nums2[j]:
                nums1[k] = nums1temp[i]
                i += 1
                k += 1      
            elif nums1temp[i] > nums2[j]:
                nums1[k] = nums2[j]
                j += 1
                k += 1
```