# Question: First Bad Version
#### Level: easy
<br>

## Question Description
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.



## Example
```
Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```
```
Example 2:

Input: n = 1, bad = 1
Output: 1
```
## Constraints
* 1 <= bad <= n <= 2^31 - 1
## 解决思路
与二分查找类似。区别在于终止条件。

## 代码(Python)
```Python
循环法（执行用时32ms，内存消耗14.8MB）
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (right - left) // 2 + left
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid) and isBadVersion(mid-1):
                right = mid - 1
            else:
                left = mid + 1
        return -1
```
```Python
迭代法（执行用时44ms，内存消耗14.8MB）【此处为保持函数格式加入一个内函数】
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        def binary_search(n, left, right):
            if left > right: 
                return -1
            mid = (left + right) // 2
            if isBadVersion(mid) and isBadVersion(mid-1):
                right = mid -1
            elif not isBadVersion(mid):
                left = mid + 1
            else:
                return mid
            return binary_search(n, left, right)
        return binary_search(n, left, right)
```