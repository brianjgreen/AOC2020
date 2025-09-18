#include "readFileToString.h"
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day20.dat"

int
day20()
{
	const char     *filename = DATA_FILE;
	char	       *fileContents = readFileToString(filename);
	int		house = 0;

	if (fileContents) {
		int		min_presents = strtol(fileContents, NULL, 10);
		//printf("%d\n", min_presents);

		int		presents = 0;

		while (presents < min_presents) {
			presents = 0;
			house++;

			for (int i = 1; i <= sqrt(house); i++) {
				if (house % i == 0) {
					presents += i * 10;
					if (i != house / i) {
						presents += (house / i) * 10;
					}
				}
			}
		}
		printf("2015 Day 20 Part 1: %d\n", house);

		house = 0;
		presents = 0;
		while (presents < min_presents) {
			presents = 0;
			house++;
			for (int i = 1; i <= (int)(round(sqrt(house))); i++) {
				if (house % i == 0) {
					if (i * 50 >= house) {
						presents += i * 11;
					}
					if ((i != house / i) && ((house / i) * 50 >= house)) {
						presents += (int)round((house / i)) * 11;
					}
				}
			}
		}
		printf("2015 Day 20 Part 2: %d\n", house);
	}

	free(fileContents);
	return 0;
}
