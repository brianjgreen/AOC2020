#include "permutations.h"
#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day13.dat"
#define PERSON_NAME_SIZE 16
#define MAX_NUM_OF_PEOPLE 16

typedef struct happy {
    char person[PERSON_NAME_SIZE];
    char sitting_next_to[PERSON_NAME_SIZE];
    int happiness;
    struct happy *next;
} happy_t;

happy_t *happy_head = NULL;
int max_happiness = 0;

char **people = NULL;
size_t guest_capacity = 0;
size_t num_people = 0;
bool dont_include_me = true;

int get_happiness(char *person_a, char *person_b) {
    int total_happiness = 0;

    for (happy_t *h = happy_head; h != NULL; h = h->next) {
        if (((strcmp(person_a, h->person) == 0) ||
             (strcmp(person_a, h->sitting_next_to) == 0)) &&
            ((strcmp(person_b, h->person) == 0) ||
             (strcmp(person_b, h->sitting_next_to) == 0))) {
            total_happiness += h->happiness;
        }
    }
    return total_happiness;
}

void add_person(char *per) {
    if (num_people > 0) {
        for (size_t i = 0; i < num_people; i++) {
            if (strcmp(people[i], per) == 0) {
                return;
            }
        }
    }

    if (num_people == guest_capacity) {
        // Increase capacity and realloc
        guest_capacity = guest_capacity == 0 ? 1 : guest_capacity * 2;
        char **new_strings = realloc(people, guest_capacity * sizeof(char *));
        if (!new_strings) {
            fprintf(stderr, "Memory allocation failed\n");
            exit(EXIT_FAILURE);
        }
        people = new_strings;
    }

    // Allocate memory for the string and copy it
    people[num_people] = malloc(strlen(per) + 1);
    if (!people[num_people]) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    strcpy(people[num_people], per);
    num_people++;
}

void add_happiness(char *person, char *sitting, int happy) {
    add_person(person);
    happy_t *per = (happy_t *)malloc(sizeof(happy_t));
    snprintf(per->person, sizeof(per->person), "%s", person);
    snprintf(per->sitting_next_to, sizeof(per->sitting_next_to), "%s", sitting);
    per->happiness = happy;
    per->next = happy_head;
    happy_head = per;
}

void print_list_of_guests(char **strings, int count) {
    // Print the permutation
    for (int i = 0; i < count; i++) {
        printf("%s ", strings[i]);
    }
    printf("\n");
}

void calc_happiness(char **table_map, int count) {
    int total_happiness = 0;
    for (int i = 1; i < count; i++) {
        total_happiness += get_happiness(table_map[i - 1], table_map[i]);
    }
    if (dont_include_me) {
        total_happiness += get_happiness(table_map[count - 1], table_map[0]);
    }
    if (total_happiness > max_happiness) {
        max_happiness = total_happiness;
    }
}

int day13() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);

    if (fileContents) {

        const char outer_delimiters[] = "\n";

        char *token;
        char *outer_saveptr = NULL;

        token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

        while (token != NULL) {

            int result;
            char person_a[PERSON_NAME_SIZE];
            char person_b[PERSON_NAME_SIZE];
            int happy_units;
            char gain_lose[] = "gain";

            result =
                /* Frank would lose 97 happiness units by sitting next to
                   Alice.*/
                sscanf(token,
                       "%s would %s %d happiness units by sitting next to %s.",
                       person_a, gain_lose, &happy_units, person_b);
            if (result != 4) {
                printf("Bad table map! %s", token);
            } else {
                person_b[strlen(person_b) - 1] = '\0';
                if (strcmp(gain_lose, "lose") == 0) {
                    happy_units *= -1;
                }
                add_happiness(person_a, person_b, happy_units);
            }

            token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
        }

        // permute(people, 0, num_people - 1, print_list_of_guests);
        permute(people, 0, num_people - 1, calc_happiness);
        printf("2015 Day 13 Part 1: %d\n", max_happiness);

        max_happiness = 0;
        dont_include_me = false;
        permute(people, 0, num_people - 1, calc_happiness);
        printf("2015 Day 13 Part 2: %d\n", max_happiness);

        free(fileContents);

        for (size_t i = 0; i < num_people; i++) {
            // printf("%s ", people[i]);
            free(people[i]);
        }
        free(people);

        printf("\n");
        for (happy_t *h = happy_head; h != NULL;) {
            happy_t *temp = h;
            // printf("%s %s %d\n", temp->point_a, temp->point_b,
            // temp->distance);
            h = h->next;
            free(temp);
        }
    }

    return 0;
}