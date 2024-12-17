//
// Advent of Code 2024 Day 9
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

func get_combo_operand(operand string, a int, b int, c int) (int, int) {
	err := 0
	num := 0
	switch operand {
	case "0", "1", "2", "3":
		// Combo operands 0 through 3 represent literal values 0 through 3.
		num, _ = strconv.Atoi(operand)
	case "4":
		// Combo operand 4 represents the value of register A.
		num = a
	case "5":
		// Combo operand 5 represents the value of register B.
		num = b
	case "6":
		// Combo operand 6 represents the value of register C.
		num = c
	default:
		// Combo operand 7 is reserved and will not appear in valid programs.
		fmt.Println("INVALID OPERAND!!!")
		err = -1
	}

	return num, err
}

func runProgram(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		// fmt.Println(err)
		return
	}

	reg_a := 0
	reg_b := 0
	reg_c := 0
	ip := 0
	program := []string{}

	for _, line := range lines {
		// fmt.Println(line)
		fields := strings.Fields(line)
		if len(fields) <= 0 {
			continue
		}
		data := fields[len(fields)-1]
		if strings.Contains(line, "Register A") {
			reg_a, _ = strconv.Atoi(data)
		} else if strings.Contains(line, "Register B") {
			reg_b, _ = strconv.Atoi(data)
		} else if strings.Contains(line, "Register C") {
			reg_c, _ = strconv.Atoi(data)
		} else if strings.Contains(line, "Program") {
			program = strings.Split(data, ",")
		}
	}
	fmt.Println("a:", reg_a, "b:", reg_b, "c:", reg_c, "ip:", ip, "prog:", program)
	output := []int{}

	for ip >= 0 && ip < len(program) {
		operand, _ := strconv.Atoi(program[ip+1])
		combo, _ := get_combo_operand(program[ip+1], reg_a, reg_b, reg_c)

		switch program[ip] {
		case "0":
			// The adv instruction (opcode 0) performs division.
			// The numerator is the value in the A register.
			// The denominator is found by raising 2 to the power of the instruction's combo operand.
			// (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.)
			// The result of the division operation is truncated to an integer and then written to the A register.
			reg_a /= int(math.Pow(2, float64(combo)))
		case "1":
			// The bxl instruction (opcode 1) calculates the bitwise XOR of register B
			// and the instruction's literal operand, then stores the result in register B.
			reg_b ^= operand
		case "2":
			// The bst instruction (opcode 2) calculates the value of its combo operand modulo 8
			// (thereby keeping only its lowest 3 bits), then writes that value to the B register.
			reg_b = combo % 8
		case "3":
			// The jnz instruction (opcode 3) does nothing if the A register is 0.
			// However, if the A register is not zero,
			// it jumps by setting the instruction pointer to the value of its literal operand;
			// if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
			if reg_a != 0 {
				ip = operand - 2
			}
		case "4":
			// The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C,
			// then stores the result in register B.
			// (For legacy reasons, this instruction reads an operand but ignores it.)
			reg_b ^= reg_c
		case "5":
			// The out instruction (opcode 5) calculates the value of its combo operand modulo 8,
			// then outputs that value. (If a program outputs multiple values, they are separated by commas.)
			output = append(output, combo%8)
		case "6":
			// The bdv instruction (opcode 6) works exactly like the adv instruction
			// except that the result is stored in the B register.
			// (The numerator is still read from the A register.)
			reg_b = reg_a / int(math.Pow(2, float64(combo)))
		case "7":
			// The cdv instruction (opcode 7) works exactly like the adv instruction
			// except that the result is stored in the C register.
			// (The numerator is still read from the A register.)
			reg_c = reg_a / int(math.Pow(2, float64(combo)))
		}
		ip += 2
	}
	fmt.Println(output)
	fmt.Print(filename, " ")
	for _, num := range output {
		fmt.Print(num, ",")
	}
	fmt.Println("\b \b")
}

func main() {
	runProgram("data.dat")
	runProgram("example.dat")
}
