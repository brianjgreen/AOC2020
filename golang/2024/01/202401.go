//
// Advent of Code 2024 Day 1
// Brian Green
//

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
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

func sortDiff(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	total := 0
	p2_total := 0

	left := []int{}
	right := []int{}

	for _, line := range lines {
		nums := strings.Fields(line)
		leftnum, _ := strconv.Atoi(nums[0])
		rightnum, _ := strconv.Atoi(nums[1])
		left = append(left, leftnum)
		right = append(right, rightnum)
	}

	sort.Ints(left)
	sort.Ints(right)
	// fmt.Println("left", left, "right", right)

	for pos, num := range left {
		total += int(math.Abs(float64(num - right[pos])))

		sim := 0
		for _, freq := range right {
			if freq == num {
				sim += 1
			}
		}
		p2_total += num * sim
	}
	fmt.Println(filename, "Total =", total)
	fmt.Println(filename, "P2 Total =", p2_total)
}

func main() {
	sortDiff("data.dat")
	sortDiff("example.dat")
}
