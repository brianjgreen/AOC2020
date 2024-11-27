//
// Advent of Code 2023 Day 2
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

func dicePower(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	total := 0

	for _, line := range lines {
		maxRed := 0
		maxGreen := 0
		maxBlue := 0
		gameSummary := strings.Split(line, ": ")
		games := strings.Split(gameSummary[1], "; ")
		for _, g := range games {
			gg := strings.Split(g, ", ")
			for _, dice := range gg {
				die := strings.Split(dice, " ")
				dNum, _ := strconv.Atoi(string(die[0]))
				color := die[1]
				if color == "red" && dNum > maxRed {
					maxRed = dNum
				}
				if color == "green" && dNum > maxGreen {
					maxGreen = dNum
				}
				if color == "blue" && dNum > maxBlue {
					maxBlue = dNum
				}
			}
		}
		total += maxBlue * maxGreen * maxRed
	}

	fmt.Printf("%s Power Total %d\n", filename, total)
}

func possibleGames(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	// only 12 red cubes, 13 green cubes, and 14 blue cubes
	maxRed := 12
	maxGreen := 13
	maxBlue := 14

	total := 0

	for _, line := range lines {
		gameSummary := strings.Split(line, ": ")
		gameRound := strings.Split(gameSummary[0], " ")
		gameNum, _ := strconv.Atoi(gameRound[1])
		possible := true
		games := strings.Split(gameSummary[1], "; ")
		for _, g := range games {
			gg := strings.Split(g, ", ")
			for _, dice := range gg {
				die := strings.Split(dice, " ")
				dNum, _ := strconv.Atoi(string(die[0]))
				color := die[1]
				if color == "red" && dNum > maxRed {
					possible = false
				}
				if color == "green" && dNum > maxGreen {
					possible = false
				}
				if color == "blue" && dNum > maxBlue {
					possible = false
				}
			}
		}
		if possible {
			total += gameNum
		}
	}

	fmt.Printf("%s Possible Total %d\n", filename, total)
}

func main() {
	possibleGames("example.dat")
	possibleGames("data.dat")
	dicePower("example.dat")
	dicePower("data.dat")
}
