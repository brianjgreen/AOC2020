//
// Advent of Code 2024 Day 9
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

func calcDiskChksum(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		// fmt.Println(err)
		return
	}

	disk_img := []int{}
	unfrag_image := [][]int{}

	for _, line := range lines {
		free_space := false
		block := 0
		for _, sector := range line {
			num, _ := strconv.Atoi(string(sector))
			unfrag := []int{}
			if free_space {
				free_space = false
				for num > 0 {
					disk_img = append(disk_img, -1)
					unfrag = append(unfrag, -1)
					num--
				}
			} else {
				free_space = true
				for num > 0 {
					disk_img = append(disk_img, block)
					unfrag = append(unfrag, block)
					num--
				}
				block++
			}
			unfrag_image = append(unfrag_image, unfrag)
			//fmt.Println(unfrag_image)
		}
	}

	// fmt.Println(disk_img)
	free_space := true
	target := -1
	for free_space {
		free_space = false
		next_free := -1
		for i, num := range disk_img {
			if num == target {
				next_free = i
				free_space = true
				break
			}
		}
		if !free_space {
			break
		}
		disk_img[next_free] = disk_img[len(disk_img)-1]
		disk_img = disk_img[:len(disk_img)-1]
	}
	// fmt.Println(disk_img)

	total := 0
	for i, num := range disk_img {
		total += i * num
	}
	fmt.Println(filename, "total:", total)

	for i := len(unfrag_image) - 1; i >= 0; i-- {
		//fmt.Println(unfrag_image[i])
		if len(unfrag_image[i]) <= 0 || unfrag_image[i][0] == -1 {
			continue
		}
		for j := range i {
			num_free := 0
			for _, k := range unfrag_image[j] {
				if k == -1 {
					num_free++
				}
			}
			if num_free >= len(unfrag_image[i]) {
				f := 0
				for k := range len(unfrag_image[i]) {
					//fmt.Println(i, j, k)
					for unfrag_image[j][f] != -1 {
						f++
					}
					unfrag_image[j][f] = unfrag_image[i][k]
					unfrag_image[i][k] = -1
				}
				break
			}
		}
	}
	// fmt.Println(unfrag_image)

	counter := 0
	p2_total := 0
	for _, i := range unfrag_image {
		for _, j := range i {
			if j == -1 {
				counter++
				continue
			}
			p2_total += counter * j
			counter++
		}
	}
	fmt.Println(filename, "P2 total:", p2_total)
}

func main() {
	calcDiskChksum("data.dat")
	calcDiskChksum("example.dat")
}
