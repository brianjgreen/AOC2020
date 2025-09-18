#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day15.dat"
#define INGREDIENT_NAME_SIZE 16

typedef struct ingredient {
	char		name[INGREDIENT_NAME_SIZE];
	int		capacity;
	int		durability;
	int		flavor;
	int		texture;
	int		calories;
	int		count;
	struct ingredient *next;
}		ingredient_t;

//Sugar:capacity 3, durability 0, flavor 0, texture - 3, calories 2

ingredient_t * ingredient_head = NULL;
int		max_score = 0;
int		max_500cal_score = 0;

void
add_ingredient(char *name, int capacity, int durability, int flavor,
	       int texture, int calories)
{
	ingredient_t   *ingr = (ingredient_t *) malloc(sizeof(ingredient_t));
	snprintf(ingr->name, sizeof(ingr->name), "%s", name);
	ingr->capacity = capacity;
	ingr->durability = durability;
	ingr->flavor = flavor;
	ingr->texture = texture;
	ingr->calories = calories;
	ingr->count = 0;
	ingr->next = ingredient_head;
	ingredient_head = ingr;
}

int
day15()
{
	const char     *filename = DATA_FILE;
	char	       *fileContents = readFileToString(filename);

	if (fileContents) {

		const char	outer_delimiters[] = "\n";

		char	       *token;
		char	       *outer_saveptr = NULL;

		token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

		while (token != NULL) {

			int		result;
			char		name[INGREDIENT_NAME_SIZE];
			int		capacity;
			int		durability;
			int		flavor;
			int		texture;
			int		calories;

	//Sugar:	capacity 3, durability 0, flavor 0, texture - 3, calories 2
				result = sscanf(token,
			    "%[^:]: capacity %d, durability %d, flavor %d, "
						"texture %d, calories %d",
			    name, &capacity, &durability, &flavor, &texture,
						&calories);
			if (result != 6) {
				printf("Bad recipe!! %d %s\n", result, token);
			} else {
				add_ingredient(name, capacity, durability, flavor, texture,
					       calories);
			}

			token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
		}

		bool		roll_over = false;
		while (!roll_over) {
			roll_over = true;
			int		total = 0;
			int		cap = 0;
			int		dur = 0;
			int		fla = 0;
			int		tex = 0;
			int		cal = 0;
			for (ingredient_t * i = ingredient_head; i != NULL; i = i->next) {
				if (roll_over) {
					if (i->count == 100) {
						i->count = 0;
					} else {
						roll_over = false;
						i->count++;
					}
				}
				total += i->count;
				cap += i->count * i->capacity;
				dur += i->count * i->durability;
				fla += i->count * i->flavor;
				tex += i->count * i->texture;
				cal += i->count * i->calories;
			}
			if (total != 100) {
				continue;
			} else {
				if ((cap > 0) && (dur > 0) && (fla > 0) && (tex > 0)) {
					int		score = cap * dur * fla * tex;
					if (score > max_score) {
						max_score = score;
					}
					if ((cal == 500) && (score > max_500cal_score)) {
						max_500cal_score = score;
					}
				}
			}
		}

		for (ingredient_t * i = ingredient_head; i != NULL;) {
			ingredient_t   *temp = i;
			/*
			 * printf("%s %d %d %d %d %d\n", temp->name,
			 * temp->capacity, temp->durability, temp->flavor,
			 * temp->texture, temp->calories);
			 */
			i = i->next;
			free(temp);
		}
	}

	printf("2015 Day 15 Part 1: %d\n", max_score);
	printf("2015 Day 15 Part 2: %d\n", max_500cal_score);

	free(fileContents);
	return 0;
}
