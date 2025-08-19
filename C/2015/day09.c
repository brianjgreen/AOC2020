#include "permutations.h"
#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day09.dat"
#define LOCATION_NAME_SIZE 16
#define MAX_NUM_OF_LOCATIONS 16

typedef struct distance {
    char point_a[LOCATION_NAME_SIZE];
    char point_b[LOCATION_NAME_SIZE];
    int distance;
    struct distance *next;
} distance_t;

distance_t *dist_head = NULL;
int max_distance = 0;
int min_distance = 1000000;

char **locations = NULL;
size_t capacity = 0;
size_t num_locations = 0;

void add_map(char *point_a, char *point_b, int distance) {
    distance_t *dist = (distance_t *)malloc(sizeof(distance_t));
    snprintf(dist->point_a, sizeof(dist->point_a), "%s", point_a);
    snprintf(dist->point_b, sizeof(dist->point_b), "%s", point_b);
    dist->distance = distance;
    dist->next = dist_head;
    dist_head = dist;
}

int get_distance(char *point_a, char *point_b) {
    for (distance_t *d = dist_head; d != NULL; d = d->next) {
        if (((strcmp(point_a, d->point_a) == 0) ||
             (strcmp(point_a, d->point_b) == 0)) &&
            ((strcmp(point_b, d->point_a) == 0) ||
             (strcmp(point_b, d->point_b) == 0))) {
            return d->distance;
        }
    }
    printf("ERROR! Cannot find distance for %s %s", point_a, point_b);
    return 0;
}

void add_location(char *loc) {
    if (num_locations > 0) {
        for (size_t i = 0; i < num_locations; i++) {
            if (strcmp(locations[i], loc) == 0) {
                return;
            }
        }
    }

    if (num_locations == capacity) {
        // Increase capacity and realloc
        capacity = capacity == 0 ? 1 : capacity * 2;
        char **new_strings = realloc(locations, capacity * sizeof(char *));
        if (!new_strings) {
            fprintf(stderr, "Memory allocation failed\n");
            exit(EXIT_FAILURE);
        }
        locations = new_strings;
    }

    // Allocate memory for the string and copy it
    locations[num_locations] = malloc(strlen(loc) + 1);
    if (!locations[num_locations]) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    strcpy(locations[num_locations], loc);
    num_locations++;
}

void print_list(char **strings, int count) {
    // Print the permutation
    for (int i = 0; i < count; i++) {
        printf("%s ", strings[i]);
    }
    printf("\n");
}

void calc_distance(char **dest_map, int count) {
    int total_distance = 0;
    for (int i = 1; i < count; i++) {
        total_distance += get_distance(dest_map[i - 1], dest_map[i]);
    }
    if (total_distance > max_distance) {
        max_distance = total_distance;
    }
    if (total_distance < min_distance) {
        min_distance = total_distance;
    }
}

int day09() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);

    if (fileContents) {

        const char outer_delimiters[] = "\n";

        char *token;
        char *outer_saveptr = NULL;

        token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

        while (token != NULL) {

            int result;
            char point_a[16];
            char point_b[16];
            int distance;
            result =
                sscanf(token, "%s to %s = %d", point_a, point_b, &distance);
            if (result != 3) {
                printf("Bad map! %s", token);
            } else {
                add_map(point_a, point_b, distance);
                add_location(point_a);
                add_location(point_b);
            }

            token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
        }

        permute(locations, 0, num_locations - 1, calc_distance);
        printf("2015 Day 09 Part 1: %d\n", min_distance);
        printf("2015 Day 09 Part 2: %d\n", max_distance);

        free(fileContents);

        for (size_t i = 0; i < num_locations; i++) {
            // printf("%s ", locations[i]);
            free(locations[i]);
        }
        free(locations);

        // printf("\n");
        for (distance_t *d = dist_head; d != NULL;) {
            distance_t *temp = d;
            // printf("%s %s %d\n", temp->point_a, temp->point_b,
            // temp->distance);
            d = d->next;
            free(temp);
        }
    }

    return 0;
}