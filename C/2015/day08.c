#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day08.dat"

enum dimentions {
	LENGTH = 0, WIDTH, HEIGHT
};

int
day08()
{
	const char     *filename = DATA_FILE;
	char	       *fileContents = readFileToString(filename);

	if (fileContents) {
		//printf("%s\n", fileContents);

		int		total_chars = 0;
		int		total_memory = 0;
		int		total_encode = 0;

		const char	outer_delimiters[] = "\n";

		char	       *token;
		char	       *outer_saveptr = NULL;

		token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

		while (token != NULL) {
			int		str_size = strlen(token);
			total_chars += str_size;
			int		mem = str_size - 2;
			int		encode = str_size + 4;
			//printf("Outer Token: %s size=%ld\n", token, strlen(token));
			char	       *c = token;
			c++;
			for (int i = 1; i < (str_size - 2); i++, c++) {
				if (*c == '\\') {
					encode += 2;
					mem--;
					c++;
					i++;
					if (*c == 'x') {
						mem -= 2;
						encode--;
					}
				}
			}

			total_memory += mem;
			total_encode += encode;
			token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
		}

		printf("2015 Day 08 Part 1: %d\n", (total_chars - total_memory));
		printf("2015 Day 08 Part 2: %d\n", (total_encode - total_chars));

		free(fileContents);
	}

	return 0;
}
