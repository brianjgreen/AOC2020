//
// Advent of Code 2024 Day 4
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

func numMasInX(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		// fmt.Println(err)
		return
	}

	total := 0
	puzzle := []string{}

	puzzle = append(puzzle, lines...) // this is kinda cool, does not need loop

	max_x := len(puzzle[0])
	max_y := len(puzzle)

	for x := range max_x {
		if x == 0 || x > max_x-2 {
			continue
		}
		for y := range max_y {
			if y == 0 || y > max_y-2 {
				continue
			}

			if string(puzzle[y][x]) == "A" {
				if (string(puzzle[y-1][x-1]) == "M" && string(puzzle[y+1][x+1]) == "S") || (string(puzzle[y-1][x-1]) == "S" && string(puzzle[y+1][x+1]) == "M") {
					if (string(puzzle[y+1][x-1]) == "M" && string(puzzle[y-1][x+1]) == "S") || (string(puzzle[y+1][x-1]) == "S" && string(puzzle[y-1][x+1]) == "M") {
						total++
					}
				}
			}
		}
	}

	fmt.Println(filename, "P2 total:", total)
}

func numXmas(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		// fmt.Println(err)
		return
	}

	total := 0
	puzzle := []string{}

	// left and right
	for _, line := range lines {
		// fmt.Println(line)
		total += strings.Count(line, "XMAS") + strings.Count(line, "SAMX")
		// fmt.Println("total=", total)
		puzzle = append(puzzle, line)
	}

	max_x := len(puzzle[0])
	max_y := len(puzzle)
	// fmt.Println("x:", max_x, "y:", max_y)

	// up and down
	for col := range max_x {
		line := ""
		for _, y := range puzzle {
			// fmt.Println("y]col[]", y, col, string(y[col]))
			line += string(y[col])
		}

		total += strings.Count(line, "XMAS") + strings.Count(line, "SAMX")
		// fmt.Println("total=", total)
	}

	// diagnal bottom left to upper right, upper left
	for y := range max_y {
		line := ""
		x := 0
		temp_y := y
		for temp_y >= 0 && x < max_x {
			// fmt.Println(line, x, temp_y, y)
			line += string(puzzle[temp_y][x])
			temp_y--
			x++
		}

		total += strings.Count(line, "XMAS") + strings.Count(line, "SAMX")
	}

	// diagnal bottom left to upper right, lower right
	for x := range max_x {
		if x == 0 {
			continue
		}

		line := ""
		y := max_y - 1
		temp_x := x
		for y >= 0 && temp_x < max_x {
			// fmt.Println(line, x, temp_y, y)
			line += string(puzzle[y][temp_x])
			temp_x++
			y--
		}

		total += strings.Count(line, "XMAS") + strings.Count(line, "SAMX")
	}

	// diagnal upper left to lower right, bottom left
	for y := range max_y {
		line := ""
		x := 0
		temp_y := y
		for temp_y < max_y && x < max_x {
			// fmt.Println(line, x, temp_y, y)
			line += string(puzzle[temp_y][x])
			temp_y++
			x++
		}

		total += strings.Count(line, "XMAS") + strings.Count(line, "SAMX")
	}

	// diagnal upper left to lower right, top right
	for x := range max_x {
		if x == 0 {
			continue
		}

		line := ""
		y := 0
		temp_x := x
		for y < max_y && temp_x < max_x {
			// fmt.Println(line, x, temp_y, y)
			line += string(puzzle[y][temp_x])
			temp_x++
			y++
		}

		total += strings.Count(line, "XMAS") + strings.Count(line, "SAMX")
	}

	fmt.Println(filename, "total:", total)
}

func main() {
	// numSupportTLS("data.dat")
	numXmas("data.dat")
	numXmas("example.dat")
	numXmas("example2.dat")
	numMasInX("example3.dat")
	numMasInX("example4.dat")
	numMasInX("data.dat")
}
