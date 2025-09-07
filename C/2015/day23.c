#include "readFileToString.h"
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day23.dat"

#define MAX_INSTR_SIZE 16

typedef struct instr {
    char instr[MAX_INSTR_SIZE];
    struct instr *next;
    struct instr *prev;
} instruction_t;

instruction_t *instr_pointer = NULL;
instruction_t *base = NULL;

void add_instruction(char *instr) {
    instruction_t *i = (instruction_t *)malloc(sizeof(instruction_t));
    snprintf(i->instr, sizeof(i->instr), "%s", instr);
    i->next = NULL;
    i->prev = base;
    if (base != NULL) {
        base->next = i;
    }
    base = i;
}

void jump_ip(int move) {
    bool forward = true;
    if (move < 0) {
        forward = false;
        move = abs(move);
    }
    for (int i = move; i != 0; i--) {
        if (forward) {
            instr_pointer = instr_pointer->next;
        } else {
            instr_pointer = instr_pointer->prev;
        }
    }
}

int value_b(int a) {
    int b = 0;

    while (instr_pointer != NULL) {
        if (strncmp(instr_pointer->instr, "hlf", 3) == 0) {
            // hlf r sets register r to half its current value, then continues
            // with the next instruction.
            if (instr_pointer->instr[4] == 'a') {
                a /= 2;
            } else {
                b /= 2;
            }
            instr_pointer = instr_pointer->next;
        } else if (strncmp(instr_pointer->instr, "tpl", 3) == 0) {
            // tpl r sets register r to triple its current value, then continues
            // with the next instruction.
            if (instr_pointer->instr[4] == 'a') {
                a *= 3;
            } else {
                b *= 3;
            }
            instr_pointer = instr_pointer->next;
        } else if (strncmp(instr_pointer->instr, "inc", 3) == 0) {
            // inc r increments register r, adding 1 to it, then continues with
            // the next instruction.
            if (instr_pointer->instr[4] == 'a') {
                a++;
            } else {
                b++;
            }
            instr_pointer = instr_pointer->next;
        } else if (strncmp(instr_pointer->instr, "jmp", 3) == 0) {
            // jmp offset is a jump; it continues with the instruction offset
            // away relative to itself.
            int move = (int)strtol(instr_pointer->instr + 4, NULL, 10);
            jump_ip(move);
        } else if (strncmp(instr_pointer->instr, "jie", 3) == 0) {
            // jie r, offset is like jmp, but only jumps if register r is even
            // ("jump if even").
            if (((instr_pointer->instr[4] == 'a') && (a % 2 == 0)) ||
                ((instr_pointer->instr[4] == 'b') && (b % 2 == 0))) {
                int move = (int)strtol(instr_pointer->instr + 7, NULL, 10);
                jump_ip(move);
            } else {
                instr_pointer = instr_pointer->next;
            }
        } else if (strncmp(instr_pointer->instr, "jio", 3) == 0) {
            // jio r, offset is like jmp, but only jumps if register r is 1
            // ("jump if one", not odd).
            if (((instr_pointer->instr[4] == 'a') && (a == 1)) ||
                ((instr_pointer->instr[4] == 'b') && (b == 1))) {
                int move = (int)strtol(instr_pointer->instr + 7, NULL, 10);
                jump_ip(move);
            } else {
                instr_pointer = instr_pointer->next;
            }
        } else {
            printf("WHAT? %s\n", instr_pointer->instr);
            instr_pointer = instr_pointer->next;
        }
    }

    return b;
}

int day23() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);

    if (fileContents) {

        const char outer_delimiters[] = "\n";

        char *token;
        char *outer_saveptr = NULL;

        token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

        while (token != NULL) {
            // printf("%s\n", token);

            add_instruction(token);

            token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
        }

        instr_pointer = base;
        while (instr_pointer->prev != NULL) {
            instr_pointer = instr_pointer->prev;
        }

        printf("2015 Day 23 Part 1: %d\n", value_b(0));

        instr_pointer = base;
        while (instr_pointer->prev != NULL) {
            instr_pointer = instr_pointer->prev;
        }
        printf("2015 Day 23 Part 2: %d\n", value_b(1));

        instr_pointer = base;
        while (instr_pointer->prev != NULL) {
            instruction_t *temp = instr_pointer;
            instr_pointer = instr_pointer->prev;
            free(temp);
        }
    }

    free(fileContents);
    return 0;
}