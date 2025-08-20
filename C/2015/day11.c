#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day11.dat"

static char alpha[] = "abcdefghjkmnpqrstuvwxyz";

/*
 *
 * 1.) Passwords must include one increasing straight of at least three
 * letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters;
 * abd doesn't count.
 * 2.) Passwords may not contain the letters i, o, or l, as
 * these letters can be mistaken for other characters and are therefore
 * confusing.
 * 3.) Passwords must contain at least two different, non-overlapping
 * pairs of letters, like aa, bb, or zz.
 *
 */

#define LAST_CHAR_OF_PASSWORD 7

void inc_password(char **password) {
    bool done = false;
    char *pos = *password + LAST_CHAR_OF_PASSWORD;

    while (!done) {
        if (*pos == 'z') {
            *pos-- = 'a';
        } else {
            done = true;
            char *next = strchr(alpha, *pos);
            if (next == NULL) {
                printf("FAILED TO FIND %c in %s", *pos, alpha);
            } else {
                *pos = *++next;
            }
        }
    }
}

bool has_straight_of_three(char *password) {
    char triple[] = "abc";
    char *ptr = alpha + 2;

    while (true) {
        if (strstr(password, triple)) {
            return true;
        }
        if (triple[2] == 'z') {
            return false;
        }
        triple[0] = triple[1];
        triple[1] = triple[2];
        triple[2] = *++ptr;
    }
    return false;
}

bool has_two_pairs(char *password) {
    int count = 0;
    char pair[] = "aa";
    char *ptr = alpha;

    while (count < 2) {
        if (strstr(password, pair)) {
            count++;
        }
        if (pair[0] == 'z') {
            break;
        }
        ptr++;
        pair[0] = *ptr;
        pair[1] = *ptr;
    }

    if (count == 2) {
        return true;
    }
    return false;
}

void find_valid_password(char **password) {
    bool is_valid = false;

    while (!is_valid) {
        inc_password(password);
        if ((has_two_pairs(*password)) && (has_straight_of_three(*password))) {
            is_valid = true;
        }
    }
}

int day11() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);

    if (fileContents) {
        printf("%s\n", fileContents);

        find_valid_password(&fileContents);
        printf("2015 Day 11 Part 1: %s\n", fileContents);

        find_valid_password(&fileContents);
        printf("2015 Day 11 Part 2: %s\n", fileContents);

        free(fileContents);
    }

    return 0;
}