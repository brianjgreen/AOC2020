//
// Advent of Code 2024 Day 14
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

type Robot struct {
	Pos_X  int
	Pos_Y  int
	Velo_X int
	Velo_Y int
}

func printRobots(robots []Robot) {
	field := [103][101]string{}
	for y := range len(field) {
		for x := range len(field[0]) {
			field[y][x] = "."
		}
	}

	for _, r := range robots {
		field[r.Pos_Y][r.Pos_X] = "#"
	}

	for _, y := range field {
		fmt.Println(y)
	}
}

func calcQuad(robots []Robot, max_x int, max_y int) int {
	quad := []int{0, 0, 0, 0}
	for _, r := range robots {
		x := r.Pos_X
		y := r.Pos_Y
		mid_x := max_x / 2
		mid_y := max_y / 2
		if x < mid_x && y < mid_y {
			quad[0]++
		} else if x > mid_x && y < mid_y {
			quad[1]++
		} else if x < mid_x && y > mid_y {
			quad[2]++
		} else if x > mid_x && y > mid_y {
			quad[3]++
		}
	}
	return quad[0] * quad[1] * quad[2] * quad[3]
}

func calcRobots(filename string, max_x int, max_y int, max_iter int) {
	lines, err := readFileLines(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	robots := []Robot{}

	for _, line := range lines {
		p := strings.Split(line, " ")
		po := strings.Split(p[0], "=")
		pos := strings.Split(po[1], ",")
		v := strings.Split(p[1], "=")
		ve := strings.Split(v[1], ",")
		px, _ := strconv.Atoi(pos[0])
		py, _ := strconv.Atoi(pos[1])
		vx, _ := strconv.Atoi(ve[0])
		vy, _ := strconv.Atoi(ve[1])
		robots = append(robots, Robot{Pos_X: px, Pos_Y: py, Velo_X: vx, Velo_Y: vy})
	}

	// fmt.Println(robots)

	i := 0
	danger := 0
	for i < max_iter {
		for j, r := range robots {
			r.Pos_X += r.Velo_X
			r.Pos_Y += r.Velo_Y
			for r.Pos_X < 0 {
				r.Pos_X += max_x
			}
			for r.Pos_X >= max_x {
				r.Pos_X -= max_x
			}
			for r.Pos_Y < 0 {
				r.Pos_Y += max_y
			}
			for r.Pos_Y >= max_y {
				r.Pos_Y -= max_y
			}
			robots[j] = r
		}
		if max_iter > 100 {
			calc_danger := calcQuad(robots, max_y, max_y)
			if danger == 0 {
				danger = calc_danger
			}
			if calc_danger < danger {
				danger = calc_danger
				fmt.Println("danger", danger)
				printRobots(robots)
				fmt.Println(i + 1)
			}
		}
		i++
	}

	fmt.Println(filename, calcQuad(robots, max_x, max_y))
}

func main() {
	calcRobots("data.dat", 101, 103, 101*103)
	calcRobots("data.dat", 101, 103, 100)
	calcRobots("example.dat", 11, 7, 100)
}
