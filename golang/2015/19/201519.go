//
// Advent of Code 2015 Day 19
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

// findAllIndices returns a slice of indices where the substring is found in the original string.
func findAllIndices(original, sub string) []int {
	var indices []int
	n := len(original)
	m := len(sub)
	for i := 0; i <= n-m; i++ {
		if original[i:i+m] == sub {
			indices = append(indices, i)
		}
	}
	return indices
}

func numMols(filename string) {
	lines, err := readFileLines(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	start_mol := ""
	orig := []string{}
	new := []string{}
	unique_mols := []string{}

	for _, line := range lines {
		formula := strings.Fields(line)
		// fmt.Println(formula, "len", len(formula))
		mol_len := len(formula)
		if mol_len == 3 {
			orig = append(orig, formula[0])
			new = append(new, formula[2])
		} else if mol_len == 1 {
			start_mol = formula[0]
		}
	}

	for m, mole := range orig {
		index := findAllIndices(start_mol, mole)
		// fmt.Println("mole", mole, "index", index)
		for _, i := range index {
			//fmt.Println(start_mol[:i], new[m], start_mol[i+len(mole):])
			new_mol := strings.Join([]string{start_mol[:i], start_mol[i+len(mole):]}, new[m])
			// fmt.Println(new_mol)
			add_mol := true
			for _, ele := range unique_mols {
				if ele == new_mol {
					add_mol = false
				}
			}
			if add_mol {
				unique_mols = append(unique_mols, new_mol)
			}
		}
	}
	fmt.Println(filename, "total", len(unique_mols))
}

func main() {
	numMols("data.dat")
	numMols("example.dat")
}
