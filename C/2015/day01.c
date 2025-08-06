#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day01.dat"

int day01() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);

    if (fileContents) {
        // printf("%s\n", fileContents);
        int floor = 0;
        int position = 0;
        bool first_time = true;
        char *move = fileContents;
        for (unsigned long i = 0; i < strlen(fileContents); i++, move++) {
            position++;
            if (*move == ')') {
                floor--;
            } else {
                floor++;
            }
            if ((floor == -1) && (first_time == true)) {
                first_time = false;
                printf("2015 Day 01 Part 2: %d\n", position);
            }
            // printf("%c", *move);
        }

        printf("2015 Day 01 Part 1: %d\n", floor);
        free(fileContents);
    }

    return 0;
}