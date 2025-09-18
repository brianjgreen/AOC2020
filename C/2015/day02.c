#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day02.dat"

enum dimentions {
	LENGTH = 0, WIDTH, HEIGHT
};

int
day02()
{
	const char     *filename = DATA_FILE;
	char	       *fileContents = readFileToString(filename);

	if (fileContents) {
		//printf("%s\n", fileContents);

		int		total_area = 0;
		int		total_ribbon = 0;

		const char	outer_delimiters[] = "\n";
		const char	inner_delimiters[] = "x";

		char	       *token;
		char	       *outer_saveptr = NULL;
		char	       *inner_saveptr = NULL;

		token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

		while (token != NULL) {
			//printf("Outer Token: %s\n", token);

			char	       *inner_token =
			strtok_r(token, inner_delimiters, &inner_saveptr);

			int		i = 0;
			int		dim[] = {LENGTH, WIDTH, HEIGHT};

			while (inner_token != NULL) {
				//printf("Inner Token: %s\n", inner_token);
				dim[i++] = atoi(inner_token);
				inner_token = strtok_r(NULL, inner_delimiters, &inner_saveptr);
			}

			int		smallest = dim[LENGTH] * dim[WIDTH];
			total_area += 2 * smallest;
			int		width_height = dim[WIDTH] * dim[HEIGHT];
			smallest = smallest < width_height ? smallest : width_height;
			total_area += 2 * width_height;
			int		height_length = dim[HEIGHT] * dim[LENGTH];
			smallest = smallest < height_length ? smallest : height_length;
			total_area += 2 * height_length;
			total_area += smallest;

			smallest = 2 * dim[LENGTH] + 2 * dim[WIDTH];
			width_height = 2 * dim[WIDTH] + 2 * dim[HEIGHT];
			smallest = smallest < width_height ? smallest : width_height;
			height_length = 2 * dim[HEIGHT] + 2 * dim[LENGTH];
			smallest = smallest < height_length ? smallest : height_length;
			total_ribbon += dim[LENGTH] * dim[WIDTH] * dim[HEIGHT];
			total_ribbon += smallest;

			token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
		}

		printf("2015 Day 02 Part 1: %d\n", total_area);
		printf("2015 Day 02 Part 2: %d\n", total_ribbon);

		free(fileContents);
	}

	return 0;
}
