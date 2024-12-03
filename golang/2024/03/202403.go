//
// Advent of Code 2024 Day 3
// Brian Green
//

package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
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

func extractNums(instr string) (int, int) {
	re := regexp.MustCompile(`\d+`)
	values := re.FindAllString(instr, -1)
	v1, _ := strconv.Atoi(values[0])
	v2, _ := strconv.Atoi(values[1])
	return v1, v2
}

func getAllMulInstr(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	total := 0
	p2_total := 0
	enable_mul := true

	// Part 1 - find and execute multiply instructions
	for _, line := range lines {
		re := regexp.MustCompile(`mul\(\d+,\d+\)`) // Tested on https://regex101.com/
		matches := re.FindAllString(line, -1)
		// fmt.Println(matches)
		for _, v := range matches {
			v1, v2 := extractNums(v)
			total += v1 * v2
		}
	}
	fmt.Println(filename, "total", total)

	// Part 2 - check do()/don't() to enable/disable mul() instructions
	for _, line := range lines {
		re := regexp.MustCompile(`mul\(\d+,\d+\)|do\(\)|don't\(\)`) // Tested on https://regex101.com/
		matches := re.FindAllString(line, -1)
		// fmt.Println(matches)
		for _, v := range matches {
			if v == "do()" {
				enable_mul = true
			} else if v == "don't()" {
				enable_mul = false
			} else {
				if enable_mul {
					v1, v2 := extractNums(v)
					p2_total += v1 * v2
				}
			}
		}
	}
	fmt.Println(filename, "P2 total", p2_total)

}

func main() {
	getAllMulInstr("data.dat")
	getAllMulInstr("example.dat")
	getAllMulInstr("example2.dat")
}
