//
// Advent of Code 2024 Day 8
// Brian Green
//

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
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

type Ant struct {
	Name  rune
	Pos_X int
	Pos_Y int
}

func findAnts(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		// fmt.Println(err)
		return
	}

	ants := []Ant{}
	max_y := len(lines)
	max_x := len(lines[0])
	antinodes := []Ant{}

	for y, line := range lines {
		for x, spot := range line {
			if spot != '.' {
				ants = append(ants, Ant{Name: spot, Pos_X: x, Pos_Y: y})
			}
		}
	}

	for _, a := range ants {
		for _, b := range ants {
			if a.Name == b.Name && a != b {
				anti := Ant{Name: ' ', Pos_X: a.Pos_X + (a.Pos_X - b.Pos_X), Pos_Y: a.Pos_Y + (a.Pos_Y - b.Pos_Y)}
				if anti.Pos_X >= 0 && anti.Pos_X < max_x && anti.Pos_Y >= 0 && anti.Pos_Y < max_y && !slices.Contains(antinodes, anti) {
					antinodes = append(antinodes, anti)
				}
			}
		}
	}
	// fmt.Println(max_x, max_y, ants)
	fmt.Println(antinodes)
	fmt.Println(filename, len(antinodes))
}

func main() {
	findAnts("data.dat")
	findAnts("example.dat")
}
