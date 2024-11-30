//
// Advent of Code 2015 Day 21
// Brian Green
//

package main

import (
	"fmt"
)

func playerWin(player_def int, player_att int) bool {
	player_hp := 100
	boss_hp := 100
	boss_def := 2
	boss_att := 8

	for player_hp > 0 && boss_hp > 0 {
		boss_hp -= player_att - boss_def
		if boss_hp > 0 {
			player_hp -= boss_att - player_def
		}
	}

	return player_hp > 0
}

func main() {
	/*
		Weapons:    Cost  Damage  Armor
		Dagger        8     4       0
		Shortsword   10     5       0
		Warhammer    25     6       0
		Longsword    40     7       0
		Greataxe     74     8       0

		Armor:      Cost  Damage  Armor
		Leather      13     0       1
		Chainmail    31     0       2
		Splintmail   53     0       3
		Bandedmail   75     0       4
		Platemail   102     0       5

		Rings:      Cost  Damage  Armor
		Damage +1    25     1       0
		Damage +2    50     2       0
		Damage +3   100     3       0
		Defense +1   20     0       1
		Defense +2   40     0       2
		Defense +3   80     0       3
	*/

	type Item struct {
		Name   string
		Cost   int
		Damage int
		Armor  int
	}

	weapons := []Item{
		{"Dagger", 8, 4, 0},
		{"Shortsword", 10, 5, 0},
		{"Warhammer", 25, 6, 0},
		{"Longsword", 40, 7, 0},
		{"Greataxe", 74, 8, 0},
	}

	armor := []Item{
		{"None", 0, 0, 0},
		{"Leather", 13, 0, 1},
		{"Chainmail", 31, 0, 2},
		{"Splintmail", 53, 0, 3},
		{"Bandedmail", 75, 0, 4},
		{"Platemail", 102, 0, 5},
	}

	rings := []Item{
		{"None", 0, 0, 0},
		{"Damage +1", 25, 1, 0},
		{"Damage +2", 50, 2, 0},
		{"Damage +3", 100, 3, 0},
		{"Defense +1", 20, 0, 1},
		{"Defense +2", 40, 0, 2},
		{"Defense +3", 80, 0, 3},
	}

	min_cost := 1000000
	max_cost := 0
	min_r1 := "None"
	min_r2 := "None"
	min_w := "None"
	min_a := "None"
	max_r1 := "None"
	max_r2 := "None"
	max_w := "None"
	max_a := "None"
	for _, r1 := range rings {
		for _, r2 := range rings {
			if !(r1.Cost == 0 && r2.Cost == 0) && r1.Cost == r2.Cost {
				continue
			}
			for _, w := range weapons {
				for _, a := range armor {
					player_win := playerWin(r1.Armor+r2.Armor+a.Armor, r1.Damage+r2.Damage+w.Damage)
					cost := r1.Cost + r2.Cost + a.Cost + w.Cost
					fmt.Println("r1:", r1.Name, "r2:", r2.Name, "w:", w.Name, "a:", a.Name, "win:", player_win)
					if player_win && cost < min_cost {
						min_cost = cost
						min_a = a.Name
						min_r1 = r1.Name
						min_r2 = r2.Name
						min_w = w.Name
					}
					if !player_win && cost > max_cost {
						max_cost = cost
						max_a = a.Name
						max_r1 = r1.Name
						max_r2 = r2.Name
						max_w = w.Name
					}
				}
			}
		}
	}

	fmt.Println("r1:", min_r1, "r2:", min_r2, "w:", min_w, "a:", min_a, "cost:", min_cost)
	fmt.Println("r1:", max_r1, "r2:", max_r2, "w:", max_w, "a:", max_a, "cost:", max_cost)
}
