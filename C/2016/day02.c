#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day02.dat"

int keypad[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

#define MAX_X 2
#define MAX_Y 2

int keypad_p2[5][5] = {{0, 0, 1, 0, 0},
                       {0, 2, 3, 4, 0},
                       {5, 6, 7, 8, 9},
                       {0, 0xA, 0xB, 0xC, 0},
                       {0, 0, 0xD, 0, 0}};

#define MAX_X_P2 4
#define MAX_Y_P2 4

int day02() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);

    if (fileContents) {
        const char outer_delimiters[] = "\n";

        char *token;
        char *outer_saveptr = NULL;

        token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

        int x = 1;
        int y = 1;
        int x_p2 = 0;
        int y_p2 = 2;

        printf("2016 Day 02\nPart (1) (2)\n");
        while (token != NULL) {

            for (char *move = token; *move != '\0'; move++) {
                int delta_x = 0;
                int delta_y = 0;
                switch (*move) {
                case 'U':
                    delta_y = -1;
                    break;
                case 'D':
                    delta_y = 1;
                    break;
                case 'R':
                    delta_x = 1;
                    break;
                case 'L':
                    delta_x = -1;
                    break;
                default:
                    printf("WHAT? %c\n", *move);
                }

                x += delta_x;
                y += delta_y;

                if (x < 0) {
                    x = 0;
                } else if (x > MAX_X) {
                    x = MAX_X;
                }

                if (y < 0) {
                    y = 0;
                } else if (y > MAX_Y) {
                    y = MAX_Y;
                }

                x_p2 += delta_x;
                y_p2 += delta_y;

                if (x_p2 < 0) {
                    x_p2 = 0;
                } else if (x_p2 > MAX_X_P2) {
                    x_p2 = MAX_X_P2;
                }

                if (y_p2 < 0) {
                    y_p2 = 0;
                } else if (y_p2 > MAX_Y_P2) {
                    y_p2 = MAX_Y_P2;
                }

                if (keypad_p2[y_p2][x_p2] == 0) {
                    x_p2 -= delta_x;
                    y_p2 -= delta_y;
                }
            }
            printf("      %d   %x\n", keypad[y][x], keypad_p2[y_p2][x_p2]);

            token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
        }
        printf("\n");
        
        free(fileContents);
    }

    return 0;
}