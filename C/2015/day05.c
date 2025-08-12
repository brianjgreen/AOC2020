#include "readFileToString.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day05.dat"

// Define the list of substrings to search for
const char *substrings[] = {"ab", "cd", "pq", "xy"};
const int num_substrings = sizeof(substrings) / sizeof(substrings[0]);

/**
 * Checks if a string contains any of the substrings from the predefined list.
 *
 * @param str The input string.
 * @return True if the string contains any of the substrings, false otherwise.
 */
bool contains_substring(const char *str) {
    for (int i = 0; i < num_substrings; i++) {
        if (strstr(str, substrings[i]) != NULL) {
            return true;
        }
    }
    return false;
}

/**
 * Counts the number of vowels in a given string.
 *
 * @param str The input string.
 * @return The number of vowels in the string.
 */
int count_vowels(const char *str) {
    int count = 0;
    while (*str != '\0') {
        char ch = tolower(*str);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
            count++;
        }
        str++;
    }
    return count;
}

/**
 * Checks if a string contains any character that appears twice in a row.
 *
 * @param str The input string.
 * @return True if the string contains consecutive duplicates, false otherwise.
 */
bool has_consecutive_duplicates(const char *str) {
    while (*str != '\0' && *(str + 1) != '\0') {
        if (*str == *(str + 1)) {
            return true;
        }
        str++;
    }
    return false;
}

bool pair_appears_twice(const char *str) {
    int len = strlen(str);

    for (int i = 0; i < len - 1; i++) {
        char pair[3] = {str[i], str[i + 1], '\0'};
        const char *remain = str + i + 2;
        if (strstr(remain, pair) != NULL) {
            return true;
        }
    }

    return false;
}

bool repeat_with_gap(const char *str) {
    int len = strlen(str);

    for (int i = 0; i < len - 2; i++) {
        if (str[i] == str[i + 2]) {
            return true;
        }
    }

    return false;
}

int day05() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);

    if (fileContents) {
        // printf("%s\n", fileContents);

        const char outer_delimiters[] = "\n";

        char *token;
        char *outer_saveptr = NULL;

        token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

        int good = 0;
        int good_p2 = 0;

        while (token != NULL) {
            // printf("Outer Token: %s\n", token);
            bool is_good = true;
            bool is_good_p2 = true;

            if ((count_vowels(token) < 3) ||
                (!has_consecutive_duplicates(token)) ||
                (contains_substring(token))) {
                is_good = false;
            }

            if ((!pair_appears_twice(token)) || (!repeat_with_gap(token))) {
                is_good_p2 = false;
            }

            if (is_good) {
                good++;
            }

            if (is_good_p2) {
                good_p2++;
            }

            token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
        }

        printf("2015 Day 05 Part 1: %d\n", good);
        printf("2015 Day 05 Part 2: %d\n", good_p2);
        free(fileContents);
    }

    return 0;
}