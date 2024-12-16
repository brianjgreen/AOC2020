//
// Advent of Code 2024 Day 11
// Brian Green
//

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func numStones(init_stones string) {
	stones := strings.Split(init_stones, " ")
	fmt.Println(stones)
	num_stones := len(stones)
	i := 0
	for i < 75 {
		new_list := []string{}
		for _, s := range stones {
			if s == "0" {
				new_list = append(new_list, "1")
			} else if len(s)%2 == 0 {
				half := len(s) / 2
				left, _ := strconv.Atoi(s[:half])
				right, _ := strconv.Atoi(s[half:])
				new_list = append(new_list, strconv.Itoa(left))
				new_list = append(new_list, strconv.Itoa(right))
			} else {
				calc_stone, _ := strconv.Atoi(s)
				new_stone := 2024 * calc_stone
				new_list = append(new_list, strconv.Itoa(new_stone))
			}
		}
		stones = new_list
		i++
		fmt.Println(i, len(stones), len(stones)-num_stones, (len(stones)-num_stones)*100/len(stones))
		num_stones = len(stones)
	}
	fmt.Println(init_stones, "NumOfStones", len(stones))
}

func main() {
	//numStones("125 17")
	numStones("3028 78 973951 5146801 5 0 23533 857")
}
