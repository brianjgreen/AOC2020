#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day06.dat"
#define MAX_X 1000
#define MAX_Y 1000

int day06() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);
    bool lights[MAX_X][MAX_Y];
    int lights_bright[MAX_X][MAX_Y];

    if (fileContents) {
        // printf("%s\n", fileContents);
        for (int x = 0; x < MAX_X; x++) {
            for (int y = 0; y < MAX_Y; y++) {
                lights[x][y] = false;
                lights_bright[x][y] = 0;
            }
        }

        const char outer_delimiters[] = "\n";

        char *token;
        char *outer_saveptr = NULL;

        token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

        while (token != NULL) {
            char action[16];
            int start_x, start_y;
            int end_x, end_y;

            int result = sscanf(token, "turn %s %d,%d through %d,%d", action,
                                &start_x, &start_y, &end_x, &end_y);
            if (result != 5) {
                result = sscanf(token, "%s %d,%d through %d,%d", action,
                                &start_x, &start_y, &end_x, &end_y);
                if (result != 5) {
                    printf("bad parsing! %s\n", token);
                }
            }

            if (strcmp(action, "on") == 0) {
                for (int x = start_x; x < end_x + 1; x++) {
                    for (int y = start_y; y < end_y + 1; y++) {
                        lights[x][y] = true;
                        lights_bright[x][y]++;
                    }
                }
            } else if (strcmp(action, "off") == 0) {
                for (int x = start_x; x < end_x + 1; x++) {
                    for (int y = start_y; y < end_y + 1; y++) {
                        lights[x][y] = false;
                        if (lights_bright[x][y] != 0) {
                            lights_bright[x][y]--;
                        }
                    }
                }
            } else if (strcmp(action, "toggle") == 0) {
                for (int x = start_x; x < end_x + 1; x++) {
                    for (int y = start_y; y < end_y + 1; y++) {
                        if (lights[x][y]) {
                            lights[x][y] = false;
                        } else {
                            lights[x][y] = true;
                        }
                        lights_bright[x][y] += 2;
                    }
                }
            }

            token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
        }

        int lights_on = 0;
        int total_bright = 0;
        for (int x = 0; x < MAX_X; x++) {
            for (int y = 0; y < MAX_Y; y++) {
                if (lights[x][y]) {
                    lights_on++;
                }
                total_bright += lights_bright[x][y];
            }
        }
        printf("2015 Day 06 Part 1: %d\n", lights_on);
        printf("2015 Day 06 Part 2: %d\n", total_bright);
        free(fileContents);
    }

    return 0;
}