#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day03.dat"

int day03() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);

    if (fileContents) {
        const char outer_delimiters[] = "\n";

        char *token;
        char *outer_saveptr = NULL;

        token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

        int total = 0;
        int total_p2 = 0;
        int i = 0;

        while (token != NULL) {
            int results;
            int a, b, c;
            int d[3];
            int e[3];
            int f[3];

            results = sscanf(token, "%d %d %d", &a, &b, &c);
            if (results != 3) {
                printf("WHAT? %s", token);
            }

            if ((a + b > c) && (a + c > b) && (b + c > a)) {
                total++;
            }
            int j = i % 3;
            d[j] = a;
            e[j] = b;
            f[j] = c;
            if (j == 2) {
                if ((d[0] + d[1] > d[2]) && (d[1] + d[2] > d[0]) &&
                    (d[0] + d[2] > d[1])) {
                    total_p2++;
                }
                if ((e[0] + e[1] > e[2]) && (e[1] + e[2] > e[0]) &&
                    (e[0] + e[2] > e[1])) {
                    total_p2++;
                }
                if ((f[0] + f[1] > f[2]) && (f[1] + f[2] > f[0]) &&
                    (f[0] + f[2] > f[1])) {
                    total_p2++;
                }
            }
            token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
            i++;
        }
        printf("2016 Day03 Part 1: %d\n", total);
        printf("2016 Day03 Part 2: %d\n", total_p2);

        free(fileContents);
    }

    return 0;
}