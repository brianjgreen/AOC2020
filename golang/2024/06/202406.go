//
// Advent of Code 2024 Day 6
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

func numCircPAths(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		// fmt.Println(err)
		return
	}

	guard_x := -1
	guard_y := -1
	guard_x_dir := 0
	guard_y_dir := -1
	max_x := len(lines[0])
	max_y := len(lines)
	area := make([][]string, max_y)
	for col := range area {
		area[col] = make([]string, max_x)
	}

	for y, line := range lines {
		if strings.Contains(line, "^") {
			guard_y = y
			guard_x = strings.Index(line, "^")
			fmt.Println("x:", guard_x, "y:", guard_y, "xDir:", guard_x_dir, "yDir:", guard_y_dir, "GUARD!")
		}
		for x, e := range strings.Split(line, "") {
			area[y][x] = e
		}
	}

	total := 0

	for y := range max_y {
		for x := range max_x {
			if area[y][x] == "#" {
				continue
			}
			if x == guard_x && y == guard_y {
				continue
			}
			area[y][x] = "#"
			save_guard_x := guard_x
			save_guard_y := guard_y
			save_guard_x_dir := guard_x_dir
			save_guard_y_dir := guard_y_dir
			i := 1000000
			for guard_x >= 0 && guard_x < max_x && guard_y >= 0 && guard_y < max_y && i > 0 {
				//fmt.Println(guard_x, max_x, guard_y, max_y)

				if guard_y+guard_y_dir < 0 || guard_x+guard_x_dir < 0 || guard_y+guard_y_dir >= max_y || guard_x+guard_x_dir >= max_x {
					// fmt.Println("OUT")
					guard_x = save_guard_x
					guard_y = save_guard_y
					guard_x_dir = save_guard_x_dir
					guard_y_dir = save_guard_y_dir
					area[y][x] = "."
					break

				}
				for area[guard_y+guard_y_dir][guard_x+guard_x_dir] == "#" {
					if guard_x_dir == 0 && guard_y_dir == -1 {
						// was north, now east
						guard_x_dir = 1
						guard_y_dir = 0
					} else if guard_x_dir == 1 && guard_y_dir == 0 {
						// was east, now south
						guard_x_dir = 0
						guard_y_dir = 1
					} else if guard_x_dir == 0 && guard_y_dir == 1 {
						// was south, now west
						guard_x_dir = -1
						guard_y_dir = 0
					} else if guard_x_dir == -1 && guard_y_dir == 0 {
						// was west, now north
						guard_x_dir = 0
						guard_y_dir = -1
					} else {
						fmt.Println("CONFUSED GUARD!!!")
						break
					}
				}

				guard_x += guard_x_dir
				guard_y += guard_y_dir
				i--
			}
			// fmt.Println(x, y)
			// for _, a := range area {
			// 	fmt.Println(a)
			// }
			if i <= 0 {
				total++
			}
			guard_x = save_guard_x
			guard_y = save_guard_y
			guard_x_dir = save_guard_x_dir
			guard_y_dir = save_guard_y_dir
			area[y][x] = "."
		}
	}

	fmt.Println(filename, "P2 total:", total)
}

func guardPath(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		// fmt.Println(err)
		return
	}

	guard_x := -1
	guard_y := -1
	guard_x_dir := 0
	guard_y_dir := -1
	max_x := len(lines[0])
	max_y := len(lines)

	for y, line := range lines {
		if strings.Contains(line, "^") {
			guard_y = y
			guard_x = strings.Index(line, "^")
			fmt.Println("x:", guard_x, "y:", guard_y, "xDir:", guard_x_dir, "yDir:", guard_y_dir, "GUARD!")
		}
		lines[y] += " "
	}

	lines = append(lines, strings.Repeat(" ", max_x))
	lines[guard_y] = lines[guard_y][:guard_x] + "X" + lines[guard_y][guard_x+1:]
	for guard_x >= 0 && guard_x < max_x && guard_y >= 0 && guard_y < max_y {
		//fmt.Println(guard_x, max_x, guard_y, max_y)
		lines[guard_y] = lines[guard_y][:guard_x] + "X" + lines[guard_y][guard_x+1:]

		if guard_y+guard_y_dir < 0 || guard_x+guard_x_dir < 0 {
			break
		}
		if string(lines[guard_y+guard_y_dir][guard_x+guard_x_dir]) == "#" {
			if guard_x_dir == 0 && guard_y_dir == -1 {
				// was north, now east
				guard_x_dir = 1
				guard_y_dir = 0
			} else if guard_x_dir == 1 && guard_y_dir == 0 {
				// was east, now south
				guard_x_dir = 0
				guard_y_dir = 1
			} else if guard_x_dir == 0 && guard_y_dir == 1 {
				// was south, now west
				guard_x_dir = -1
				guard_y_dir = 0
			} else if guard_x_dir == -1 && guard_y_dir == 0 {
				// was west, now north
				guard_x_dir = 0
				guard_y_dir = -1
			} else {
				fmt.Println("CONFUSED GUARD!!!")
				break
			}
		}

		guard_x += guard_x_dir
		guard_y += guard_y_dir
	}

	//for _, line := range lines {
	//	fmt.Println(line)
	//}
	total := 0
	for _, line := range lines {
		total += strings.Count(line, "X")
	}
	fmt.Println(filename, "total", total)
}

func main() {
	guardPath("data.dat")
	guardPath("example.dat")
	numCircPAths("example.dat")
	numCircPAths("data.dat")
}
