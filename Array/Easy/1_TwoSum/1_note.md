# Question: Two Sum
#### Level: easy
<br>

## Question Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Example
```
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
```
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
```
```
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
```
## Constraints
* 2 <= nums.length <= 10^4
* -10^9 <= nums[i] <= 10^9
* -10^9 <= target <= 10^9
* Only one valid answer exists.

## Follow-up 
Can you come up with an algorithm that is less than `O(n^2)` time complexity?

## 解决思路
### 初始想法
简单粗暴双层遍历，若找到则返回。时间复杂度O(n^2)。

### 进一步想法
遍历一遍列表将所有元素存放在哈希表中，**key为元素，value为索引**。若存在重复元素，**后者加在前者之上**。在下一步遍历时可以找到前者，因为二者等价，且只存在唯一解，所以唯一的可能就是存在两个重复元素，target的值等于这两个重复元素的和。在遍历列表的时候会先遍历到前者，然后判断索引与哈希表中索引值是否相等，若相等则跳过，若不相等，则用哈希表中索引值减去当前索引值即为另一个重复元素的索引值。

再遍历一遍列表。用target减去当前元素值得到temp，并在哈希表中查找**除了当前元素之外**是否存在temp值，若存在则返回当前索引值和哈希表中索引值。
时间复杂度为查找哈希表的时间+遍历两次列表的时间，因此近似为O(n)。


## 代码(Python)
```Python
初始想法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return list([i,j])
        return None
```
```Python
进一步想法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashdict = {}
        for i in range(len(nums)):
            if nums[i] not in hashdict:
                hashdict[nums[i]] = i
            else:
                hashdict[nums[i]] += i
        for j in range(len(nums)):
            temp = target - nums[j]
            if temp in hashdict:
                if temp == nums[j]:
                    if hashdict[temp] == j:
                        continue
                    else:
                        return list([j,hashdict[temp]-j])
                elif temp != nums[j]:
                    return list([j,hashdict[temp]])
        return None
```