package main

import (
	"fmt"
)

// 构造一个{"string":[string, string], ... }的结构
func main() {
	strs := []string{"ddddddddddg", "dgggggggggg"}
	fmt.Println(groupAnagrams(strs))
}

func groupAnagrams(strs []string) [][]string {
	temp_map := map[[26]int][]string{}
	for _, str := range strs {
		temp_str_map := [26]int{}
		for _, char := range str {
			temp_str_map[char-'a'] += 1
		}

		if _, ok := temp_map[temp_str_map]; ok {
			temp_map[temp_str_map] = append(temp_map[temp_str_map], str)
		} else {
			temp_map[temp_str_map] = []string{str}
		}
	}

	result_slice := [][]string{}
	for _, value := range temp_map {
		result_slice = append(result_slice, value)
	}
	return result_slice
}
