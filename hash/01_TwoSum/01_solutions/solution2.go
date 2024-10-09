package main

import "fmt"

// 使用哈希表，注意到只需要查target-nums[i]
func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	fmt.Println(twoSum(nums, target))
}

func twoSum(nums []int, target int) []int {
	hash_temp := map[int]int{}
	for i, value := range nums {
		index, ok := hash_temp[target-value]
		if ok {
			return []int{index, i}
		} else {
			hash_temp[value] = i
		}
	}
	return []int{}
}
