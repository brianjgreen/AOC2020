#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day06.dat"

typedef struct column_s {
	char		letter;
	int		freq;
	struct column_s *next;
}		column_t;

typedef struct position_s {
	int		pos;
	struct position_s *next;
	column_t       *column_head;
}		position_t;

position_t     *position_head = NULL;
int		pos_num = 0;

void
add_pos()
{
	position_t     *new_pos = (position_t *) malloc(sizeof(position_t));
	new_pos->pos = pos_num;
	new_pos->column_head = NULL;
	new_pos->next = position_head;
	position_head = new_pos;
	pos_num++;
}

void
add_col(int pos, char col)
{
	position_t     *position = position_head;
	for (position_t * p = position_head; p != NULL; p = p->next) {
		if (p->pos == pos) {
			position = p;
			break;
		}
	}

	if (position->column_head == NULL) {
		column_t       *c = (column_t *) malloc(sizeof(column_t));
		c->freq = 1;
		c->letter = col;
		c->next = NULL;

		position->column_head = c;
		return;
	}

	for (column_t * c = position->column_head; c != NULL; c = c->next) {
		if (c->letter == col) {
			c->freq++;
			return;
		}
	}

	column_t       *c = (column_t *) malloc(sizeof(column_t));
	c->freq = 1;
	c->letter = col;
	c->next = position->column_head;
	position->column_head = c;
}

int
day06()
{
	const char     *filename = DATA_FILE;
	char	       *fileContents = readFileToString(filename);

	if (fileContents) {
		bool		need_positions = true;
		const char	outer_delimiters[] = "\n";

		char	       *token;
		char	       *outer_saveptr = NULL;

		token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

		while (token != NULL) {
			if (need_positions) {
				need_positions = false;
				for (size_t i = 0; i < strlen(token); i++) {
					add_pos();
				}
			}

			for (size_t i = 0; i < strlen(token); i++) {
				add_col(i, token[i]);
			}

			token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
		}

		char		freq[pos_num + 1];
		char		least[pos_num + 1];
		freq[pos_num] = '\0';
		least[pos_num] = '\0';
		pos_num--;
		for (position_t * p = position_head; p != NULL; p = p->next) {
			int		most = 0;
			int		few = 1000000;
			for (column_t * c = p->column_head; c != NULL; c = c->next) {
				if (c->freq > most) {
					most = c->freq;
					freq[pos_num] = c->letter;
				}
				if (c->freq < few) {
					few = c->freq;
					least[pos_num] = c->letter;
				}
			}
			pos_num--;
		}

		printf("2016 Day 06 Part 1: %s\n", freq);
		printf("2016 Day 06 Part 2: %s\n", least);

		for (position_t * p = position_head; p != NULL;) {
			position_t     *p_temp = p;

			for (column_t * c = p->column_head; c != NULL;) {
				column_t       *c_temp = c;
				c = c->next;
				free(c_temp);
			}

			p = p->next;
			free(p_temp);
		}

		free(fileContents);
	}
	return 0;
}
