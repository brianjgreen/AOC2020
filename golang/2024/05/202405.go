//
// Advent of Code 2024 Day 5
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

func makeValid(line string, before []string, after []string, fail_a string, fail_b string) int {
	//fmt.Println(line, "a", fail_a, "b", fail_b)
	curr_line := line
	curr_fail := fail_b
	curr_bef := fail_a
	i := 100
	for i >= 0 {
		new_line := strings.Replace(curr_line, curr_fail, string(""), 1)
		new_line = strings.Replace(new_line, curr_bef, curr_fail+","+curr_bef, 1)
		// new_line = curr_fail + "," + new_line
		new_page_pos := make(map[string]int)
		new_pages := strings.Split(new_line, ",")
		for j, p := range new_pages {
			new_page_pos[p] = j
		}
		isValid, fail_a, fail_b := isPageValid(before, after, new_page_pos, new_line)
		if !isValid {
			// fmt.Println(i, ">", new_line, "a", fail_a, "b", fail_b)
			curr_line = new_line
			curr_fail = fail_b
			curr_bef = fail_a
		} else {
			// fmt.Println("OK")
			new_line = strings.Replace(new_line, ",", " ", -1)
			pages := strings.Fields(new_line)
			mid, _ := strconv.Atoi(pages[len(pages)/2])
			return mid
		}
		i--
	}
	return -1
}

func isPageValid(before []string, after []string, page_pos map[string]int, line string) (bool, string, string) {
	isValid := true
	fail_b := ""
	fail_a := ""

	for i, b := range before {
		if strings.Contains(line, b) && strings.Contains(line, after[i]) {
			if page_pos[b] > page_pos[after[i]] {
				isValid = false
				fail_a = after[i]
				fail_b = b
				break
			}
		}
	}
	return isValid, fail_a, fail_b
}

func sumCorMidPages(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		// fmt.Println(err)
		return
	}

	total := 0
	p2_total := 0
	before := []string{}
	after := []string{}

	for _, line := range lines {
		if strings.Contains(line, "|") {
			rule := strings.Split(line, "|")
			b := rule[0]
			a := rule[1]
			before = append(before, b)
			after = append(after, a)
			continue
		}
		if line == "" {
			continue
		}

		page_pos := make(map[string]int)
		pages := strings.Split(line, ",")
		for i, p := range pages {
			page_pos[p] = i
		}

		isValid, fail_a, fail_b := isPageValid(before, after, page_pos, line)
		if isValid {
			mid, _ := strconv.Atoi(pages[len(pages)/2])
			total += mid
		} else {
			// fmt.Println(line, "a", fail_a, "b", fail_b)
			what := makeValid(line, before, after, fail_a, fail_b)
			if what == -1 {
				fmt.Println("FAIL")
			} else {
				p2_total += what
			}
		}
	}

	fmt.Println(filename, "total:", total)
	fmt.Println(filename, "P2 total:", p2_total)
}

func main() {
	sumCorMidPages("data.dat")
	sumCorMidPages("example.dat")
}
