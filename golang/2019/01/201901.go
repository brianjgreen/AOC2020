//
// Advent of Code 2019 Day 1
// Brian Green
//

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
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

func getAdditionalfuelRequired(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	total := 0

	for _, line := range lines {
		mass, _ := strconv.Atoi(line)
		// take its mass, divide by three, round down, and subtract 2
		fuelReqd := int(math.Floor(float64(mass)/3)) - 2
		total += fuelReqd

		for fuelReqd > 0 {
			fuelReqd = int(math.Floor(float64(fuelReqd)/3)) - 2
			if fuelReqd > 0 {
				total += fuelReqd
			}
		}
	}

	fmt.Printf("Additional Fuel Total = %d\n", total)
}

func getfuelRequired(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	total := 0

	for _, line := range lines {
		mass, _ := strconv.Atoi(line)
		// take its mass, divide by three, round down, and subtract 2
		total += int(math.Floor(float64(mass)/3)) - 2
	}

	fmt.Printf("Total = %d\n", total)
}

func main() {
	getfuelRequired("data.dat")
	getAdditionalfuelRequired("data.dat")
}
