#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day01.dat"

typedef struct compass_s {
    int dir;
    int x;
    int y;
    int left;
    int right;
} compass_t;

typedef struct location_s {
    int x;
    int y;
    struct location_s *next;
} location_t;

location_t *location_head = NULL;

typedef enum direction_e { NORTH = 0, EAST, SOUTH, WEST } direction_t;

compass_t movement[] = {
    {.dir = NORTH, .x = 0, .y = 1, .left = WEST, .right = EAST},
    {.dir = EAST, .x = 1, .y = 0, .left = NORTH, .right = SOUTH},
    {.dir = SOUTH, .x = 0, .y = -1, .left = EAST, .right = WEST},
    {.dir = WEST, .x = -1, .y = 0, .left = SOUTH, .right = NORTH},
};
#define MOVEMENT_SIZE (sizeof(movement) / sizeof(movement[0]))

bool already_visit(int x, int y) {
    if (location_head != NULL) {
        for (location_t *l = location_head; l != NULL; l = l->next) {
            if ((l->x == x) && (l->y == y)) {
                return true;
            }
        }
    }

    location_t *new_loc = (location_t *)malloc(sizeof(location_t));
    new_loc->x = x;
    new_loc->y = y;
    new_loc->next = location_head;
    location_head = new_loc;

    return false;
}

int day01() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);

    if (fileContents) {
        // printf("%s\n", fileContents);
        int needle = NORTH;
        int x = 0;
        int y = 0;
        int x_p2 = 0;
        int y_p2 = 0;
        bool found_dup_loc = false;

        char *move = fileContents;
        while (*move != '\0') {

            if (*move++ == 'L') {
                needle = movement[needle].left;
            } else {
                needle = movement[needle].right;
            }

            int steps = strtol(move, &move, 10);

            for (int i = steps; i > 0; i--) {
                x += movement[needle].x;
                y += movement[needle].y;
                if (!found_dup_loc) {
                    if (already_visit(x, y)) {
                        found_dup_loc = true;
                        x_p2 = x;
                        y_p2 = y;
                    }
                }
            }

            if (*move != '\0') {
                move += 2;
            }
        }

        printf("2016 Day 01 Part 1: %d\n", abs(x) + abs(y));
        printf("2016 Day 01 Part 2: %d\n", abs(x_p2) + abs(y_p2));

        free(fileContents);
        for (location_t *l = location_head; l != NULL;) {
            location_t *temp = l;
            l = l->next;
            free(temp);
        }
    }

    return 0;
}