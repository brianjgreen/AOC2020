//
// Advent of Code 2024 Day 2
// Brian Green
//

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readFileLines(filename string) ([]string, error) {
	var lines []string
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return lines, nil
}

func isSafe(nums []string) bool {
	// fmt.Println(nums)
	first_num := true
	safe := true
	dir_known := false
	dir_forward := true
	prev_num := 0
	for _, num := range nums {
		value, _ := strconv.Atoi(num)
		value = int(value)
		if first_num {
			first_num = false
			prev_num = value
		} else {
			if !dir_known {
				dir_known = true
				if value > prev_num {
					dir_forward = true
				} else if value < prev_num {
					dir_forward = false
				} else {
					safe = false
					// fmt.Println("prev", prev_num, "next", value, "equal?")
					break
				}
			}

			if value > prev_num && dir_forward {
				if value-prev_num > 3 {
					safe = false
					// fmt.Println("prev", prev_num, "next", value, "dir", dir_forward, dir_known, "wrong dir?")
					break
				}
			} else if value < prev_num && !dir_forward {
				if prev_num-value > 3 {
					safe = false
					// fmt.Println("prev", prev_num, "next", value, "dir", dir_forward, dir_known, "wrong dir?")
					break
				}
			} else {
				safe = false
				// fmt.Println("prev", prev_num, "next", value, "equal again?")
				break
			}
			prev_num = value
		}
		// fmt.Println(num)
	}

	return safe
}

func howManyTolerantSafe(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	total := 0

	for _, line := range lines {
		nums := strings.Fields(line)
		if isSafe(nums) {
			total += 1
		} else {
			// fmt.Println("len", len(nums))
			for i := range nums { // This is confusing, i is the position but not the value
				tol_nums := []string{}
				for j, num := range nums {
					if i != j {
						tol_nums = append(tol_nums, num)
					}
				}
				if isSafe(tol_nums) {
					total += 1
					break
				}
			}
		}
	}

	fmt.Println(filename, "P2 total:", total)
}

func howManySafe(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	total := 0

	for _, line := range lines {
		nums := strings.Fields(line)
		if isSafe(nums) {
			total += 1
		}
	}

	fmt.Println(filename, "total:", total)
}

func main() {
	howManySafe("data.dat")
	howManySafe("example.dat")
	howManyTolerantSafe("data.dat")
	howManyTolerantSafe("example.dat")
}
