#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define DATA_FILE "day10.dat"

char	       *
get_say_it(char *current)
{
	char	       *new_str = (char *)malloc(strlen(current) * 2);
	new_str[0] = '\0';

	int		count = 1;
	char		num_str[16];
	for (size_t i = 1; i <= strlen(current); i++) {
		if (current[i] == current[i - 1]) {
			count++;
		} else {
			snprintf(num_str, sizeof(num_str), "%d", count);
			//printf("num=%s ", num_str);
			count = 1;
			strcat(new_str, num_str);
			//printf("new=%s ", new_str);
			strncat(new_str, &current[i - 1], 1);
			//printf("%s\n", new_str);
		}
	}
	return new_str;
}

int
day10()
{
	const char     *filename = DATA_FILE;
	char	       *fileContents = readFileToString(filename);

	if (fileContents) {
		// printf("%s\n", fileContents);
		char	       *current = fileContents;

		for (int i = 2; i < 42; i++) {
			char	       *temp = current;
			current = get_say_it(temp);
			/***
	                size_t length = strlen(current);
	                // Conway's constant
	                double conway_constant = 1.303577269034;
	                // Calculate the length of the nth generation
	                double conway_length = 10 * pow(conway_constant, i - 2);
	                printf("%d: %s %ld (%lf)\n", i, current, length, conway_length);
	                ***/
			free(temp);
		}

		printf("2015 Day 10 Part 1: %ld\n", strlen(current));

		for (int i = 0; i < 10; i++) {
			char	       *temp = current;
			current = get_say_it(temp);
			free(temp);
		}
		printf("2015 Day 10 Part 2: %ld\n", strlen(current));

		//free(fileContents);
		free(current);
	}

	return 0;
}
