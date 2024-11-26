//
// Advent of Code 2023 Day 1
// Brian Green
//

package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strings"
)

// ExtractFirstAndLastDigits extracts the first and last digits from a string.
func ExtractFirstAndLastDigits(s string) (firstDigit rune, lastDigit rune, err error) {
	// Remove leading and trailing whitespace
	s = strings.TrimSpace(s)

	// Check if the string is empty after removing whitespace
	if len(s) == 0 {
		return 0, 0, errors.New("input string is empty")
	}

	// Find the first digit
	for _, r := range s {
		if '0' <= r && r <= '9' {
			firstDigit = r
			break
		}
	}

	// If no digits were found, return an error
	if firstDigit == 0 {
		return 0, 0, errors.New("no digits found in the input string")
	}

	// Find the last digit
	lastDigit = 0
	for i := len(s) - 1; i >= 0; i-- {
		r := rune(s[i])
		if '0' <= r && r <= '9' {
			lastDigit = r
			break
		}
	}

	return
}

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

func getCaliValFromAll(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Create a dictionary (map) of strings to integers
	stringToIntMap := make(map[string]string)
	stringToIntMap["one"] = "1"
	stringToIntMap["two"] = "2"
	stringToIntMap["three"] = "3"
	stringToIntMap["four"] = "4"
	stringToIntMap["five"] = "5"
	stringToIntMap["six"] = "6"
	stringToIntMap["seven"] = "7"
	stringToIntMap["eight"] = "8"
	stringToIntMap["nine"] = "9"

	total := 0

	for _, line := range lines {
		nonOverlapLine := line
		for k := range stringToIntMap {
			nonOverlapLine = strings.ReplaceAll(nonOverlapLine, k, k+string(k[len(k)-1]))
		}
		for k := range stringToIntMap {
			nonOverlapLine = strings.ReplaceAll(nonOverlapLine, k, stringToIntMap[k])
		}

		firstDigit, lastDigit, err := ExtractFirstAndLastDigits(nonOverlapLine)
		if err != nil {
			fmt.Println(err)
		} else {
			value := int(firstDigit-'0')*10 + int(lastDigit-'0')
			total += value
		}
	}

	fmt.Printf("%s Part 2 Calibration = %d\n", filename, total)
}

func getCalibrationValue(filename string) {
	// filename := "example.dat"
	lines, err := readFileLines(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	total := 0

	for _, line := range lines {
		// fmt.Println(line)
		firstDigit, lastDigit, err := ExtractFirstAndLastDigits(line)
		if err != nil {
			fmt.Println(err)
		} else {
			value := int(firstDigit-'0')*10 + int(lastDigit-'0')
			// fmt.Printf("Digits: %c %c %d\n", firstDigit, lastDigit, value)
			// fmt.Printf("Last Digit: %c\n", lastDigit)
			total += value
		}
	}

	fmt.Printf("%s Calibration = %d\n", filename, total)
}

func main() {
	getCalibrationValue("example.dat")
	getCalibrationValue("data.dat")
	getCaliValFromAll("example2.dat")
	getCaliValFromAll("data.dat")
}
