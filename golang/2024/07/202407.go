//
// Advent of Code 2024 Day 7
// Brian Green
//

package main

import (
	"bufio"
	"fmt"
	"math"
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

func isCatFormEq(answer int, values []int) bool {
	is_equal := false
	permu := generatePermutations(len(values) - 1)
	for _, p := range permu {
		if is_equal {
			break
		}
		subtotal := values[0]
		for n, j := range p {
			// fmt.Println(n, j)
			if j == 0 {
				subtotal *= values[n+1]
			} else if j == 1 {
				subtotal += values[n+1]
			} else {
				temp, _ := strconv.Atoi(strconv.Itoa(subtotal) + strconv.Itoa(values[n+1]))
				subtotal = temp
			}
		}

		if subtotal == answer {
			is_equal = true
			break
		}
	}
	return is_equal
}

func isFormEq(answer int, values []int) bool {
	is_equal := false
	permu := math.Pow(2, float64(len(values)-1))
	for i := range int(permu) {
		if is_equal {
			break
		}
		sub_total := values[0]
		for j := range len(values) - 1 {
			// fmt.Print((i >> j) & 1)
			if (i>>j)&1 == 1 {
				// fmt.Print("mul ")
				sub_total *= values[j+1]
			} else {
				// fmt.Print("add ")
				sub_total += values[j+1]
			}
		}
		if sub_total == answer {
			is_equal = true
			break
		}
		// fmt.Println()
	}
	return is_equal
}

func sumCal(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		// fmt.Println(err)
		return
	}

	total := 0
	p2_total := 0

	for _, line := range lines {
		parseCal := strings.Split(line, ":")
		answer, _ := strconv.Atoi(parseCal[0])
		data := strings.Fields(parseCal[1])
		values := []int{}
		for _, v := range data {
			val, _ := strconv.Atoi(v)
			values = append(values, val)
		}

		if isFormEq(answer, values) {
			total += answer
			p2_total += answer
		} else if isCatFormEq(answer, values) {
			p2_total += answer
		}
	}

	fmt.Println(filename, "total", total)
	fmt.Println(filename, "P2 total", p2_total)
}

func generatePermutations(n int) [][]int { // Google AI helped me write this function
	if n == 1 {
		return [][]int{{0}, {1}, {2}}
	}

	result := [][]int{}
	for _, perm := range generatePermutations(n - 1) {
		for _, digit := range []int{0, 1, 2} {
			newPerm := append([]int{digit}, perm...)
			result = append(result, newPerm)
		}
	}
	return result
}

func main() {
	sumCal("data.dat")
	sumCal("example.dat")
}
