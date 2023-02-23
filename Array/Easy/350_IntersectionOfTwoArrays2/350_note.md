# Question: Intersection of Two Arrays II
#### Level: Easy
<br>

## Question Description
Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.
## Example
```
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```
```
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
```
## Constraints
* 1 <= nums1.length, nums2.length <= 1000
* 0 <= nums1[i], nums2[i] <= 1000
## 解决思路
### 暴力搜索
双循环，每次循环后若有相同元素则去掉。
### 双指针
快排算法对array排序，然后使用双指针进行比较。
### 哈希表
将两个array均用哈希表存储，value为元素出现次数。选择长度较短的nums进行遍历，查看元素是否在另一个nums的哈希表中，并选择较小的次数作为该元素在结果array中出现的次数。
## 代码(Python)
```Python
暴力搜素
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        resultnums = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    resultnums.append(nums2[j])
                    nums2.pop(j)
                    break
        return resultnums
```
```Python
双指针
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        resultlist = []
        if len(nums1) == 0 or len(nums2) == 0:
            return resultlist
        else:
            i = 0
            j = 0
            while True:
                if i == len(nums1) or j == len(nums2):
                    break
                elif nums1[i] < nums2[j]:
                    i += 1
                elif nums1[i] == nums2[j]:
                    resultlist.append(nums1[i])
                    i += 1
                    j += 1
                elif nums1[i] > nums2[j]:
                    j += 1
            return resultlist
```
```Python
哈希表
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1dict = {}
        nums2dict = {}
        resultlist = []
        for i in range(len(nums1)):
            if nums1[i] in nums1dict:
                nums1dict[nums1[i]] += 1
            else:
                nums1dict[nums1[i]] = 1
        for j in range(len(nums2)):
            if nums2[j] in nums2dict:
                nums2dict[nums2[j]] += 1
            else:
                nums2dict[nums2[j]] = 1
        if len(nums1) < len(nums2):
            for k in range(len(nums1)):
                if nums1[k] in nums2dict:
                    if nums1[k] not in resultlist:
                        if nums1dict[nums1[k]] < nums2dict[nums1[k]]:
                            resultlist += [nums1[k]] * nums1dict[nums1[k]]
                        else:
                            resultlist += [nums1[k]] * nums2dict[nums1[k]]
                    else:
                        continue
                else:
                    continue
        else:
            for m in range(len(nums2)):
                if nums2[m] in nums1dict:
                    if nums2[m] not in resultlist:
                        if nums2dict[nums2[m]] < nums1dict[nums2[m]]:
                            resultlist += [nums2[m]] * nums2dict[nums2[m]]
                        else:
                            resultlist += [nums2[m]] * nums1dict[nums2[m]]
                    else:
                        continue
                else:
                    continue
        return resultlist
```