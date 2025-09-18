#include "readFileToString.h"
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day21.dat"

#define MAX_NAME_LEN 16

typedef struct item {
	char		name[MAX_NAME_LEN];
	int		cost;
	int		damage;
	int		armor;
}		item_t;

/*
 * Weapons:    Cost  Damage  Armor Dagger        8     4       0 Shortsword
 * 10     5       0 Warhammer    25     6       0 Longsword    40     7
 * 0 Greataxe     74     8       0
 *
 * Armor:      Cost  Damage  Armor Leather      13     0       1 Chainmail
 * 31     0       2 Splintmail   53     0       3 Bandedmail   75     0
 * 4 Platemail   102     0       5
 *
 * Rings:      Cost  Damage  Armor Damage +1    25     1       0 Damage +2
 * 50     2       0 Damage +3   100     3       0 Defense +1   20     0
 * 1 Defense +2   40     0       2 Defense +3   80     0       3
 */

item_t		weapons[] = {
	{"Dagger", 8, 4, 0}, {"Shortsword", 10, 5, 0}, {"Warhammer", 25, 6, 0},
	{"Longsword", 40, 7, 0}, {"Greataxe", 74, 8, 0},
};
#define MAX_WEAPONS (sizeof(weapons) / sizeof(weapons[0]))

item_t		armor[] = {
	{"None", 0, 0, 0}, {"Leather", 13, 0, 1},
	{"Chainmail", 31, 0, 2}, {"Splintmail", 53, 0, 3},
	{"Bandedmail", 75, 0, 4}, {"Platemail", 102, 0, 5},
};
#define MAX_ARMOR (sizeof(armor) / sizeof(armor[0]))

item_t		rings[] = {
	{"None", 0, 0, 0}, {"Damage +1", 25, 1, 0},
	{"Damage +2", 50, 2, 0}, {"Damage +3", 100, 3, 0},
	{"Defense +1", 20, 0, 1}, {"Defense +2", 40, 0, 2},
	{"Defense +3", 80, 0, 3},
};
#define MAX_RINGS (sizeof(rings) / sizeof(rings[0]))

bool
player_wins(int boss_hp, int boss_def, int boss_att, int player_def,
	    int player_att)
{
	int		player_hp = 100;
	while (player_hp > 0 && boss_hp > 0) {
		boss_hp -= player_att - boss_def;
		if (boss_hp > 0) {
			player_hp -= boss_att - player_def;
		}
	}

	return (player_hp > 0);
}

int
day21()
{
	int		boss_hp = 0;
	int		boss_att = 0;
	int		boss_def = 0;
	const char     *filename = DATA_FILE;
	char	       *fileContents = readFileToString(filename);

	if (fileContents) {

		const char	outer_delimiters[] = "\n";

		char	       *token;
		char	       *outer_saveptr = NULL;

		token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

		while (token != NULL) {
			int		result;
			char		key[] = "Hit Points";
			int		value;

			result = sscanf(token, "%[^:]: %d", key, &value);
			if (result == 2) {
				//printf("%s: %d\n", key, value);
				if (strcmp("Hit Points", key) == 0) {
					boss_hp = value;
				} else if (strcmp("Damage", key) == 0) {
					boss_att = value;
				} else if (strcmp("Armor", key) == 0) {
					boss_def = value;
				} else {
					printf("Unknown key/value %s/%d\n", key, value);
				}
			}

			token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
		}

		int		min_cost = 1000000;
		int		max_cost = 0;

		for (size_t r1 = 0; r1 < MAX_RINGS; r1++) {
			for (size_t r2 = 0; r2 < MAX_RINGS; r2++) {
				if (!(rings[r1].cost == 0 && rings[r2].cost == 0) &&
				    (rings[r1].cost == rings[r2].cost)) {
					continue;
				}
				for (size_t w = 0; w < MAX_WEAPONS; w++) {
					for (size_t a = 0; a < MAX_ARMOR; a++) {
						bool		player_won = player_wins(
						boss_hp, boss_def, boss_att,
											 rings[r1].armor + rings[r2].armor + armor[a].armor,
											 rings[r1].damage + rings[r2].damage +
							 weapons[w].damage);
						int		cost = rings[r1].cost + rings[r2].cost +
						armor[a].cost + weapons[w].cost;
						if (player_won && (cost < min_cost)) {
							min_cost = cost;
						}
						if (!player_won && (cost > max_cost)) {
							max_cost = cost;
						}
					}
				}
			}
		}
		printf("2015 Day 21 Part 1: %d\n", min_cost);
		printf("2015 Day 21 Part 2: %d\n", max_cost);
	}

	free(fileContents);
	return 0;
}
