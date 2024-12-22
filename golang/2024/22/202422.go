//
// Advent of Code 2024 Day 22
// Brian Green
//

package main

import (
	"bufio"
	"fmt"
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

func sumBuyerSecrets(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	total := 0
	max_secrets := 2000

	for _, line := range lines {
		secret, _ := strconv.Atoi(line)
		counter := max_secrets
		for counter > 0 {
			// In particular, each buyer's secret number evolves into the next secret number in the sequence via the following process:
			//	Calculate the result of multiplying the secret number by 64.
			result := secret * 64
			// Then, mix this result into the secret number.
			secret ^= result
			// Finally, prune the secret number.
			secret %= 16777216

			// Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
			result = secret / 32
			// Then, mix this result into the secret number.
			secret ^= result
			// Finally, prune the secret number.
			secret %= 16777216

			// Calculate the result of multiplying the secret number by 2048.
			result = secret * 2048
			// Then, mix this result into the secret number.
			secret ^= result
			// Finally, prune the secret number.
			secret %= 16777216

			/*
				Each step of the above process involves mixing and pruning:
				To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number.
				Then, the secret number becomes the result of that operation.
				(If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
				To prune the secret number, calculate the value of the secret number modulo 16777216.
				Then, the secret number becomes the result of that operation.
				(If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)

			*/
			counter--
		}
		total += secret
	}

	fmt.Println(filename, total)
}

func main() {
	sumBuyerSecrets("data.dat")
	sumBuyerSecrets("example.dat")
}
