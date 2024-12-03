//
// Advent of Code 2016 Day 7
// Brian Green
//

package main

import (
	"bufio"
	"fmt"
	"os"
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

func isTLS(entry string) bool {
	if entry[0] != entry[1] && entry[0] == entry[3] && entry[1] == entry[2] {
		return true
	}
	return false
}

func isSSL(entry string) bool {
	if strings.ContainsAny(entry, "[]") {
		return false
	}
	if entry[0] != entry[1] && entry[0] == entry[2] {
		return true
	}
	return false
}

func isValidSSL(i string, o string) bool {
	if i[0] == o[1] && i[1] == o[0] {
		return true
	}
	return false
}

func numSupportTLS(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		// fmt.Println(err)
		return
	}

	total := 0

	for _, addr := range lines {
		buff := "    "
		valid := false
		inside_brackets := false
		for _, c := range addr {
			buff = buff[1:] + string(c)
			if strings.Contains(buff, "[") {
				inside_brackets = true
			}
			if strings.Contains(buff, "]") {
				inside_brackets = false
			}
			if isTLS(buff) {
				if inside_brackets {
					// fmt.Println("Invalid", buff)
					valid = false
					break
				} else {
					// fmt.Println(buff)
					valid = true
				}
			}
		}
		if valid {
			total++
		}
	}

	fmt.Println(filename, "total", total)
}

func numSupportSSL(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		// fmt.Println(err)
		return
	}

	p2_total := 0

	for _, addr := range lines {
		buff := "   "
		inside_brackets := false
		outside := []string{}
		inside := []string{}
		for _, c := range addr {
			buff = buff[1:] + string(c)
			if strings.Contains(buff, "[") {
				inside_brackets = true
			}
			if strings.Contains(buff, "]") {
				inside_brackets = false
			}

			if isSSL(buff) {
				if inside_brackets {
					inside = append(inside, buff)
				} else {
					outside = append(outside, buff)
				}
			}
		}

		found_SSL := false
		// fmt.Println(inside, outside)
		for _, i := range inside {
			for _, o := range outside {
				if isValidSSL(i, o) {
					found_SSL = true
					// fmt.Println("found")
				}
			}
		}
		if found_SSL {
			p2_total++
		}
	}

	fmt.Println(filename, "P2 total", p2_total)
}

func main() {
	numSupportTLS("data.dat")
	numSupportSSL("data.dat")
	numSupportTLS("example.dat")
	numSupportSSL("example2.dat")
}
