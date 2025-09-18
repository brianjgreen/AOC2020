#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day03.dat"

typedef struct house {
	int		x;
	int		y;
	int		gifts;
	struct house   *next;
}		house_t;

house_t	       *
update_houses(int x, int y, house_t * houses)
{
	bool		house_again = false;
	for (house_t * curr_house = houses; curr_house != NULL;
	     curr_house = curr_house->next) {
		if ((curr_house->x == x) && (curr_house->y == y)) {
			house_again = true;
			curr_house->gifts++;
			break;
		}
	}
	if (!house_again) {
		house_t	       *new_house = (house_t *) malloc(sizeof(house_t));
		new_house->x = x;
		new_house->y = y;
		new_house->gifts = 1;
		new_house->next = houses;
		houses = new_house;
	}

	return houses;
}

int
day03()
{
	const char     *filename = DATA_FILE;
	char	       *fileContents = readFileToString(filename);

	if (fileContents) {
		//printf("%s\n", fileContents);

		char	       *move = fileContents;
		int		x = 0;
		int		y = 0;
		int		s1_x = 0;
		int		s1_y = 0;
		int		robo_x = 0;
		int		robo_y = 0;
		bool		robo_santa_active = false;

		house_t	       *houses = (house_t *) malloc(sizeof(house_t));
		houses->x = x;
		houses->y = y;
		houses->gifts = 1;
		houses->next = NULL;

		house_t	       *houses_robo = (house_t *) malloc(sizeof(house_t));
		houses_robo->x = x;
		houses_robo->y = y;
		houses_robo->gifts = 2;
		houses_robo->next = NULL;

		for (unsigned long i = 0; i < strlen(fileContents); i++, move++) {
			switch (*move) {
			case '>':
				x++;
				robo_santa_active ? robo_x++ : s1_x++;
				break;

			case 'v':
				y--;
				robo_santa_active ? robo_y-- : s1_y--;
				break;

			case '<':
				x--;
				robo_santa_active ? robo_x-- : s1_x--;
				break;

			case '^':
				y++;
				robo_santa_active ? robo_y++ : s1_y++;
				break;

			default:
				printf("%c unknown dir!", *move);
				break;
			}

			houses = update_houses(x, y, houses);

			if (robo_santa_active) {
				robo_santa_active = false;
				houses_robo = update_houses(robo_x, robo_y, houses_robo);
			} else {
				robo_santa_active = true;
				houses_robo = update_houses(s1_x, s1_y, houses_robo);
			}
		}

		int		total_houses = 0;
		for (house_t * curr_house = houses; curr_house != NULL;) {
			total_houses++;
			house_t	       *free_house = curr_house;
			curr_house = curr_house->next;
			free(free_house);
		}
		int		total_houses_part2 = 0;
		for (house_t * curr_house = houses_robo; curr_house != NULL;) {
			total_houses_part2++;
			house_t	       *free_house = curr_house;
			curr_house = curr_house->next;
			free(free_house);
		}

		printf("2015 Day 03 Part 1: %d\n", total_houses);
		printf("2015 Day 03 Part 2: %d\n", total_houses_part2);
		free(fileContents);
	}

	return 0;
}
