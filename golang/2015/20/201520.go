//
// Advent of Code 2015 Day 20
// Brian Green
//

package main

import (
	"fmt"
	"math"
)

func findFactors(n int) []int {
	factors := []int{}

	// Iterate up to the square root of n
	for i := 1; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			factors = append(factors, i)
			if n/i != i {
				factors = append(factors, n/i)
			}
		}
	}

	return factors
}

func main() {
	max_num := 0
	max_house := 0
	first_house := 0
	first_num := 0
	first_found := false
	p2_max_num := 0
	p2_max_house := 0
	p2_first_house := 0
	p2_first_num := 0
	p2_first_found := false
	for num := 1; num < 1000000; num++ {
		factors := findFactors(num)
		sum := 0
		p2_sum := 0
		for _, n := range factors {
			sum += n
			if n*50 >= num {
				p2_sum += n
			}
		}
		sum *= 10
		p2_sum *= 11
		if sum > max_num {
			max_house = num
			max_num = sum
		}
		if p2_sum > p2_max_num {
			p2_max_house = num
			p2_max_num = p2_sum
		}
		if !first_found && sum >= 36000000 {
			first_found = true
			first_house = num
			first_num = sum
			// break
		}
		if !p2_first_found && p2_sum >= 36000000 {
			p2_first_found = true
			p2_first_house = num
			p2_first_num = p2_sum
			// break
		}
		// fmt.Println("Factors of", num, "are:", factors, "sum:", sum)
	}
	fmt.Println("Max House", max_house, "present", max_num)
	fmt.Println("first house", first_house, "first sum", first_num)
	fmt.Println("P2 Max House", p2_max_house, "present", p2_max_num)
	fmt.Println("P2 first house", p2_first_house, "first sum", p2_first_num)
}
