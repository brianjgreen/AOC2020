#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Example function call: permute(strings, 0, count - 1);

// Function to swap two elements
void swap(char **a, char **b) {
    char *temp = *a;
    *a = *b;
    *b = temp;
}

// Function to generate all permutations of the strings array
void permute(char **strings, int start, int end,
             void (*process_permutation)(char **, int)) {
    int i;
    if (start == end) {
        process_permutation(strings, end + 1);
    } else {
        for (i = start; i <= end; i++) {
            swap(&strings[start], &strings[i]);
            permute(strings, start + 1, end, process_permutation);
            swap(&strings[start], &strings[i]); // backtrack
        }
    }
}
