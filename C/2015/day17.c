#include "readFileToString.h"
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day17.dat"

#define MAX_VOLUME 150

typedef struct container {
	int		container_size;
	struct container *next;
}		container_t;

container_t    *container_head = NULL;

void
add_container(int container_size)
{
	container_t    *c = (container_t *) malloc(sizeof(container_t));
	c->container_size = container_size;
	c->next = container_head;
	container_head = c;
}

int
day17()
{
	const char     *filename = DATA_FILE;
	char	       *fileContents = readFileToString(filename);

	if (fileContents) {

		const char	outer_delimiters[] = "\n";

		char	       *token;
		char	       *outer_saveptr = NULL;

		token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

		while (token != NULL) {
			add_container(strtol(token, NULL, 10));

			token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
		}

		int		total_containers = 0;
		for (container_t * c = container_head; c != NULL; c = c->next) {
			total_containers++;
		}

		double		bits = pow(2, total_containers);
		int		num_combos = 0;
		int		min_containers = total_containers;

		for (size_t i = 0; i < (size_t) bits; i++) {
			int		j = i;
			int		volume = 0;
			int		num_containers = 0;

			for (container_t * c = container_head; c != NULL; c = c->next) {
				if ((j & 1) == 1) {
					volume += c->container_size;
					num_containers++;
				}
				j >>= 1;
				if (volume > MAX_VOLUME) {
					break;
				}
			}

			if (volume == MAX_VOLUME) {
				num_combos++;
				if (num_containers < min_containers) {
					min_containers = num_containers;
				}
			}
		}

		printf("2015 Day 17 Part 1: %d\n", num_combos);
		printf("2015 Day 17 Part 2: %d\n", min_containers);

		for (container_t * c = container_head; c != NULL;) {
			container_t    *temp = c;
			//printf("%d ", temp->container_size);
			c = c->next;
			free(temp);
		}
	}

	free(fileContents);
	return 0;
}
