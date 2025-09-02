#include "readFileToString.h"
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day18.dat"

#define MAX_X_LIGHTS 100
#define MAX_Y_LIGHTS 100
#define OFFSET_NUM 3

const int offset[] = {-1, 0, 1};

bool init_lights[MAX_X_LIGHTS][MAX_Y_LIGHTS];
bool lights[MAX_X_LIGHTS][MAX_Y_LIGHTS];
bool next_lights[MAX_X_LIGHTS][MAX_Y_LIGHTS];

void initialize_lights(bool stuck_lights) {
    for (int x = 0; x < MAX_X_LIGHTS; x++) {
        for (int y = 0; y < MAX_Y_LIGHTS; y++) {
            lights[x][y] = init_lights[x][y];
        }
    }
    if (stuck_lights) {
        lights[0][0] = true;
        lights[0][MAX_Y_LIGHTS - 1] = true;
        lights[MAX_X_LIGHTS - 1][0] = true;
        lights[MAX_X_LIGHTS - 1][MAX_Y_LIGHTS - 1] = true;
    }
}

int get_total_on() {
    int grand_total = 0;
    for (int x = 0; x < MAX_X_LIGHTS; x++) {
        for (int y = 0; y < MAX_Y_LIGHTS; y++) {
            if (lights[x][y]) {
                grand_total++;
            }
        }
    }
    return grand_total;
}

void cycle_lights(bool stuck_lights) {
    int counter = 100;
    while (counter > 0) {
        for (int x = 0; x < MAX_X_LIGHTS; x++) {
            for (int y = 0; y < MAX_Y_LIGHTS; y++) {
                int total_on = 0;
                bool state = lights[x][y];
                for (int i = 0; i < OFFSET_NUM; i++) {
                    for (int j = 0; j < OFFSET_NUM; j++) {
                        if ((i == 1) && (j == 1)) {
                            continue;
                        }
                        int delta_x = x + offset[i];
                        int delta_y = y + offset[j];
                        if ((delta_x < 0) || (delta_x == MAX_X_LIGHTS) ||
                            (delta_y < 0) || (delta_y == MAX_Y_LIGHTS)) {
                            continue;
                        }
                        if (lights[delta_x][delta_y]) {
                            total_on++;
                        }
                    }
                }
                if (state) {
                    if ((total_on == 2) || (total_on == 3)) {
                        next_lights[x][y] = true;
                    } else {
                        next_lights[x][y] = false;
                    }
                } else {
                    if (total_on == 3) {
                        next_lights[x][y] = true;
                    } else {
                        next_lights[x][y] = false;
                    }
                }
            }
        }

        for (int x = 0; x < MAX_X_LIGHTS; x++) {
            for (int y = 0; y < MAX_Y_LIGHTS; y++) {
                lights[x][y] = next_lights[x][y];
            }
        }
        if (stuck_lights) {
            lights[0][0] = true;
            lights[0][MAX_Y_LIGHTS - 1] = true;
            lights[MAX_X_LIGHTS - 1][0] = true;
            lights[MAX_X_LIGHTS - 1][MAX_Y_LIGHTS - 1] = true;
        }
        counter--;
    }
}

int day18() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);

    if (fileContents) {

        const char outer_delimiters[] = "\n";

        char *token;
        char *outer_saveptr = NULL;

        token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

        int x = 0;
        // int y = 0;

        while (token != NULL) {
            for (int y = 0; y < MAX_Y_LIGHTS; y++) {
                init_lights[x][y] = (token[y] == '#');
            }

            x++;
            token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
        }

        initialize_lights(false);
        cycle_lights(false);
        printf("2015 Day 18 Part 1: %d\n", get_total_on());

        initialize_lights(true);
        cycle_lights(true);
        printf("2015 Day 18 Part 2: %d\n", get_total_on());
    }

    free(fileContents);
    return 0;
}