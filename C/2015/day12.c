#include "readFileToString.h"
#include <cjson/cJSON.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day12.dat"

double get_numbers(cJSON *item, bool exclude_red) {
    cJSON *current = NULL;
    if (!item) {
        return 0;
    }

    if (item->type == cJSON_Number) {
        return item->valuedouble;
    } else if ((item->type == cJSON_Array) || (item->type == cJSON_Object)) {
        double total = 0;
        current = item->child;
        while (current) {
            if ((exclude_red) && (item->type == cJSON_Object) &&
                ((current->type == cJSON_String) &&
                 (strcmp(current->valuestring, "red") == 0))) {
                return 0;
            }
            total += get_numbers(current, exclude_red);
            current = current->next;
        }
        return total;
    }
    return 0;
}

int day12() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);

    if (fileContents) {
        // printf("%s\n", fileContents);
        cJSON *root = cJSON_Parse(fileContents);
        if (root == NULL) {
            const char *error_ptr = cJSON_GetErrorPtr();
            if (error_ptr != NULL) {
                fprintf(stderr, "Error before: %s\n", error_ptr);
            }
            free(fileContents);
            return -1;
        }

        double sum_of_all_nums = get_numbers(root, false);
        // printf("%s\n", cJSON_Print(root));
        printf("2015 Day 12 Part 1: %.0lf\n", sum_of_all_nums);

        sum_of_all_nums = get_numbers(root, true);
        printf("2015 Day 12 Part 2: %.0lf\n", sum_of_all_nums);

        cJSON_Delete(root);
        free(fileContents);
    }

    return 0;
}