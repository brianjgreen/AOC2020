#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day04.dat"

typedef struct symb_freq_s {
	char		symb;
	int		freq;
	struct symb_freq_s *next;
}		symb_freq_t;

symb_freq_t    *symb_head = NULL;

void
add_symb(char symb)
{
	if (symb_head != NULL) {
		for (symb_freq_t * s = symb_head; s != NULL; s = s->next) {
			if (s->symb == symb) {
				s->freq++;
				return;
			}
		}
	}
	symb_freq_t    *new_symb = (symb_freq_t *) malloc(sizeof(symb_freq_t));
	new_symb->symb = symb;
	new_symb->freq = 1;
	new_symb->next = symb_head;
	symb_head = new_symb;
}

void
del_symb(char symb)
{
	if (symb_head->symb == symb) {
		symb_freq_t    *temp = symb_head;
		symb_head = symb_head->next;
		free(temp);
		return;
	}

	symb_freq_t    *prev = symb_head;
	for (symb_freq_t * temp = symb_head->next; temp != NULL;
	     prev = temp, temp = temp->next) {
		if (temp->symb == symb) {
			prev->next = temp->next;
			free(temp);
			return;
		}
	}
}

int
day04()
{
	const char     *filename = DATA_FILE;
	char	       *fileContents = readFileToString(filename);

	if (fileContents) {
		const char	outer_delimiters[] = "\n";

		char	       *token;
		char	       *outer_saveptr = NULL;

		token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

		int		total_sectors = 0;

		while (token != NULL) {
			int		dashes = 0;
			int		total_dashes = 0;
			for (char *c = token; *c != '\0'; c++) {
				if (*c == '-') {
					dashes++;
				}
			}
			total_dashes = dashes;
			char	       *t = token;
			while (dashes > 0) {
				if (*t == '-') {
					dashes--;
				} else {
					add_symb(*t);
				}
				t++;
			}
			int		results;
			int		sector_id;
			char		checksum[16];
			results = sscanf(t, "%d[%s]", &sector_id, checksum);
			if (results != 2) {
				printf("WHAT? %c", *t);
			}

			bool		valid_room = true;
			for (char *check = checksum; *check != ']'; check++) {
				symb_freq_t	most_freq = {.symb = '{',.freq = 0,.next = NULL};
				for (symb_freq_t * s = symb_head; s != NULL; s = s->next) {
					if (s->freq > most_freq.freq) {
						most_freq.symb = s->symb;
						most_freq.freq = s->freq;
					} else if ((s->freq == most_freq.freq) &&
					       (s->symb < most_freq.symb)) {
						most_freq.symb = s->symb;
					}
				}
				if (most_freq.symb != *check) {
					valid_room = false;
					break;
				}
				del_symb(most_freq.symb);
			}

			if (valid_room) {
				total_sectors += sector_id;

				char		room_name[128];
				char	       *room = room_name;

				t = token;
				dashes = total_dashes;
				while (dashes > 0) {
					if (*t == '-') {
						*room++ = ' ';
						dashes--;
					} else {
						char		x = ((*t - 'a' + (sector_id % 26)) % 26) + 'a';
						*room++ = x;
					}
					t++;
				}
				*room = '\0';
				if (strstr(room_name, "north") != NULL) {
					printf("2016 Day04 Part 2: %s %d\n", room_name, sector_id);
				}
				//printf("%s\n", room_name);
			}

			//Free linked list
				for (symb_freq_t * s = symb_head; s != NULL;) {
				symb_freq_t    *temp = s;
				s = s->next;
				free(temp);
			}
			symb_head = NULL;
			token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
		}
		printf("2016 Day04 Part 1: %d\n", total_sectors);
		free(fileContents);
	}
	return 0;
}
