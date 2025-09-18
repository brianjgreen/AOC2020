#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day16.dat"
#define PRESENT_NAME_SIZE 16
#define NUM_OF_PRESENTS 3

typedef struct sue {
	int		sue_num;
	int		children;
	int		cats;
	int		samoyeds;
	int		pomeranians;
	int		akitas;
	int		vizslas;
	int		goldfish;
	int		trees;
	int		cars;
	int		perfumes;
	struct sue     *next;
}		sue_t;

//Sue 1:goldfish:6, trees:9, akitas:0

sue_t * sue_head = NULL;

void
add_sue(int sue_num, int children, int cats, int samoyeds, int pomeranians,
	int akitas, int vizslas, int goldfish, int trees, int cars,
	int perfumes)
{
	sue_t	       *sue = (sue_t *) malloc(sizeof(sue_t));
	sue->sue_num = sue_num;
	sue->children = children;
	sue->cats = cats;
	sue->samoyeds = samoyeds;
	sue->pomeranians = pomeranians;
	sue->akitas = akitas;
	sue->vizslas = vizslas;
	sue->goldfish = goldfish;
	sue->trees = trees;
	sue->cars = cars;
	sue->perfumes = perfumes;
	sue->next = sue_head;
	sue_head = sue;
}

int
day16()
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
			int		sue_num;
			int		children = -1;
			int		cats = -1;
			int		samoyeds = -1;
			int		pomeranians = -1;
			int		akitas = -1;
			int		vizslas = -1;
			int		goldfish = -1;
			int		trees = -1;
			int		cars = -1;
			int		perfumes = -1;
			char		present[NUM_OF_PRESENTS][PRESENT_NAME_SIZE];
			int		p[NUM_OF_PRESENTS];

	//Sue 1:goldfish:6, trees:9, akitas:0
				result = sscanf(token, "Sue %d: %[^:]: %d, %[^:]: %d, %[^:]: %d",
			     &sue_num, present[0], &p[0], present[1], &p[1],
						present[2], &p[2]);
			if (result != 7) {
				printf("Bad thank you list!! %d %s\n", result, token);
			} else {
				for (int i = 0; i < NUM_OF_PRESENTS; i++) {
					if (strcmp(present[i], "children") == 0) {
						children = p[i];
					} else if (strcmp(present[i], "cats") == 0) {
						cats = p[i];
					} else if (strcmp(present[i], "samoyeds") == 0) {
						samoyeds = p[i];
					} else if (strcmp(present[i], "pomeranians") == 0) {
						pomeranians = p[i];
					} else if (strcmp(present[i], "akitas") == 0) {
						akitas = p[i];
					} else if (strcmp(present[i], "vizslas") == 0) {
						vizslas = p[i];
					} else if (strcmp(present[i], "goldfish") == 0) {
						goldfish = p[i];
					} else if (strcmp(present[i], "trees") == 0) {
						trees = p[i];
					} else if (strcmp(present[i], "cars") == 0) {
						cars = p[i];
					} else if (strcmp(present[i], "perfumes") == 0) {
						perfumes = p[i];
					} else {
						printf("Unknown present! %s", present[i]);
					}
				}
				add_sue(sue_num, children, cats, samoyeds, pomeranians, akitas,
				  vizslas, goldfish, trees, cars, perfumes);
			}

			token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
		}

		sue_t		aunt_sue = {.children = 3,
			.cats = 7,
			.samoyeds = 2,
			.pomeranians = 3,
			.akitas = 0,
			.vizslas = 0,
			.goldfish = 5,
			.trees = 3,
			.cars = 2,
		.perfumes = 1};

		for (sue_t * s = sue_head; s != NULL; s = s->next) {
			if ((s->children != -1) && (aunt_sue.children != s->children)) {
				continue;
			} else if ((s->cats != -1) && (aunt_sue.cats != s->cats)) {
				continue;
			} else if ((s->samoyeds != -1) &&
				   (aunt_sue.samoyeds != s->samoyeds)) {
				continue;
			} else if ((s->pomeranians != -1) &&
				 (aunt_sue.pomeranians != s->pomeranians)) {
				continue;
			} else if ((s->akitas != -1) && (aunt_sue.akitas != s->akitas)) {
				continue;
			} else if ((s->vizslas != -1) && (aunt_sue.vizslas != s->vizslas)) {
				continue;
			} else if ((s->goldfish != -1) &&
				   (aunt_sue.goldfish != s->goldfish)) {
				continue;
			} else if ((s->trees != -1) && (aunt_sue.trees != s->trees)) {
				continue;
			} else if ((s->cars != -1) && (aunt_sue.cars != s->cars)) {
				continue;
			} else if ((s->perfumes != -1) &&
				   (aunt_sue.perfumes != s->perfumes)) {
				continue;
			}

			printf("2015 Day 16 Part 1: %d\n", s->sue_num);
		}

		/*
		 * the cats and trees readings indicates that there are
		 * greater than that many, the pomeranians and goldfish
		 * readings indicate that there are fewer than that many
		 *
		 */
		for (sue_t * s = sue_head; s != NULL; s = s->next) {
			if ((s->children != -1) && (aunt_sue.children != s->children)) {
				continue;
			} else if ((s->cats != -1) && (aunt_sue.cats > s->cats)) {
				continue;
			} else if ((s->samoyeds != -1) &&
				   (aunt_sue.samoyeds != s->samoyeds)) {
				continue;
			} else if ((s->pomeranians != -1) &&
				   (aunt_sue.pomeranians < s->pomeranians)) {
				continue;
			} else if ((s->akitas != -1) && (aunt_sue.akitas != s->akitas)) {
				continue;
			} else if ((s->vizslas != -1) && (aunt_sue.vizslas != s->vizslas)) {
				continue;
			} else if ((s->goldfish != -1) &&
				   (aunt_sue.goldfish < s->goldfish)) {
				continue;
			} else if ((s->trees != -1) && (aunt_sue.trees > s->trees)) {
				continue;
			} else if ((s->cars != -1) && (aunt_sue.cars != s->cars)) {
				continue;
			} else if ((s->perfumes != -1) &&
				   (aunt_sue.perfumes != s->perfumes)) {
				continue;
			}

			printf("2015 Day 16 Part 2: %d\n", s->sue_num);
			break;
		}

		for (sue_t * s = sue_head; s != NULL;) {
			sue_t	       *temp = s;
			/***
	                printf("%d %d %d %d %d %d %d %d %d %d %d\n", temp->sue_num,
	                temp->children, temp->cats, temp->samoyeds, temp->pomeranians,
	                       temp->akitas, temp->vizslas, temp->goldfish, temp->trees,
	                temp->cars, temp->perfumes);
	                       ***/
			s = s->next;
			free(temp);
		}
	}

	//printf("2015 Day 15 Part 1: %d\n", max_score);
	//printf("2015 Day 15 Part 2: %d\n", max_500cal_score);

	free(fileContents);
	return 0;
}
