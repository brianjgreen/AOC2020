#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day14.dat"
#define DEER_NAME_SIZE 16

typedef struct flight {
	char		name[DEER_NAME_SIZE];
	int		speed;
	int		fly;
	int		rest;
	bool	       *pattern;
	int		distance;
	int		points;
	struct flight  *next;
}		flight_t;

// Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.

		flight_t * flight_head = NULL;
int		max_deer_distance = 0;
int		max_points = 0;

void
add_deer(char *name, int speed, int fly, int rest)
{
	flight_t       *deer = (flight_t *) malloc(sizeof(flight_t));
	snprintf(deer->name, sizeof(deer->name), "%s", name);
	deer->speed = speed;
	deer->fly = fly;
	deer->rest = rest;
	deer->distance = 0;
	deer->points = 0;
	deer->pattern = malloc(sizeof(bool) * (fly + rest));
	for (int i = 0; i < fly; i++) {
		deer->pattern[i] = true;
	}
	for (int i = fly; i < (fly + rest); i++) {
		deer->pattern[i] = false;
	}
	deer->next = flight_head;
	flight_head = deer;
}

void
deer_race(int seconds)
{
	for (int i = 0; i < seconds; i++) {
		int		max_dist = 0;
		for (flight_t * f = flight_head; f != NULL; f = f->next) {
			if (f->pattern[i % (f->fly + f->rest)]) {
				f->distance += f->speed;
			}
			if (f->distance > max_deer_distance) {
				max_deer_distance = f->distance;
			}
			if (f->distance > max_dist) {
				max_dist = f->distance;
			}
		}
		for (flight_t * f = flight_head; f != NULL; f = f->next) {
			if (max_dist == f->distance) {
				f->points++;
			}
			if (f->points > max_points) {
				max_points = f->points;
			}
		}
	}
}

int
day14()
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
			char		name[DEER_NAME_SIZE];
			int		speed;
			int		fly;
			int		rest;

			// Vixen can fly 8 km / s for 8 seconds, but then must rest for 53 seconds.
						result = sscanf(token,
								"%s can fly %d km/s for %d seconds, but then must "
						     "rest for %d seconds.",
						 name, &speed, &fly, &rest);
			if (result != 4) {
				printf("Bad flight info!! %s", token);
			} else {
				add_deer(name, speed, fly, rest);
			}

			token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
		}

		deer_race(2503);

		for (flight_t * f = flight_head; f != NULL;) {
			flight_t       *temp = f;
			//printf("%s %d %d %d %d %d\n", temp->name, temp->speed, temp->fly,
				 //temp->rest, temp->distance, temp->points);
			f = f->next;
			//free(temp->name);
			//free(temp->pattern);
			free(temp);
		}
	}

	printf("2015 Day 14 Part 1: %d\n", max_deer_distance);
	printf("2015 Day 14 Part 2: %d\n", max_points);

	free(fileContents);
	return 0;
}
