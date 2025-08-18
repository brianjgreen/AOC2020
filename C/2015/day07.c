#include "readFileToString.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day07.dat"
// #define DATA_FILE "day07_test.dat"

typedef enum operations { NONE, MOV, AND, OR, LSHIFT, RSHIFT, NOT } ops;

typedef struct wire {
    char name[4];
    ops op;
    char input_a[8];
    char input_b[8];
    bool value_valid;
    unsigned short value;
    bool p2_value_valid;
    unsigned short p2_value;
    struct wire *next;
} wire_t;

wire_t *wire_head = NULL;

wire_t *create_wire(char *name) {
    wire_t *wire = (wire_t *)malloc(sizeof(wire_t));

    snprintf(wire->name, sizeof(wire->name), "%s", name);
    wire->op = NONE;
    snprintf(wire->input_a, sizeof(wire->input_a), "%s", name);
    snprintf(wire->input_b, sizeof(wire->input_b), "%s", name);
    wire->value_valid = false;
    wire->value = 0;
    wire->p2_value_valid = false;
    wire->p2_value = 0;
    wire->next = wire_head;

    wire_head = wire;

    return wire;
}

wire_t *get_wire(char *name) {
    for (wire_t *wire = wire_head; wire != NULL; wire = wire->next) {
        if (strcmp(wire->name, name) == 0) {
            return wire;
        }
    }

    return create_wire(name);
}

unsigned short get_wire_value(bool is_part2, wire_t *wire) {
    unsigned short inp1, inp2, temp;

    if (wire == NULL) {
        printf("NULL!\n");
        return 0;
    }

    if ((!is_part2) && (wire->value_valid)) {
        return wire->value;
    } else if ((is_part2) && (wire->p2_value_valid)) {
        return wire->p2_value;
    }

    temp = strtoul(wire->input_a, NULL, 10);
    if (strcmp(wire->input_a, "0") == 0) {
        inp1 = 0;
    } else if (temp != 0) {
        inp1 = temp;
    } else {
        inp1 = get_wire_value(is_part2, get_wire(wire->input_a));
    }
    temp = strtoul(wire->input_b, NULL, 10);
    if (strcmp(wire->input_b, "0") == 0) {
        inp2 = 0;
    } else if (temp != 0) {
        inp2 = temp;
    } else {
        inp2 = get_wire_value(is_part2, get_wire(wire->input_b));
    }

    if (is_part2) {
        wire->p2_value_valid = true;
    } else {
        wire->value_valid = true;
    }

    unsigned short value;
    switch (wire->op) {
    case MOV:
        value = inp1;
        break;
    case NOT:
        value = (~inp1);
        break;
    case AND:
        value = (inp1 & inp2);
        break;
    case OR:
        value = (inp1 | inp2);
        break;
    case LSHIFT:
        value = (inp1 << inp2);
        break;
    case RSHIFT:
        value = (inp1 >> inp2);
        break;
    default:
        printf("UNKNOWN OPERATION! %s\n", wire->name);
        if (is_part2) {
            wire->p2_value_valid = false;
        } else {
            wire->value_valid = false;
        }
        return 0;
    }

    if (is_part2) {
        wire->p2_value = value;
    } else {
        wire->value = value;
    }
    return value;
}

void update_wire(wire_t *wire, ops op, char *input_a, char *input_b) {
    wire->op = op;
    snprintf(wire->input_a, sizeof(wire->input_a), "%s", input_a);
    snprintf(wire->input_b, sizeof(wire->input_b), "%s", input_b);
}

ops name_to_op(char *op_name) {
    if (strcmp(op_name, "OR") == 0) {
        return OR;
    } else if (strcmp(op_name, "AND") == 0) {
        return AND;
    } else if (strcmp(op_name, "RSHIFT") == 0) {
        return RSHIFT;
    } else if (strcmp(op_name, "LSHIFT") == 0) {
        return LSHIFT;
    } else if (strcmp(op_name, "NOT") == 0) {
        return NOT;
    } else {
        printf("UKNOWN OPERATION %s\n", op_name);
    }
    return NONE;
}

char *op_to_name(ops op) {
    switch (op) {
    case OR:
        return "OR";
        break;
    case AND:
        return "AND";
        break;
    case RSHIFT:
        return "RSHIFT";
        break;
    case LSHIFT:
        return "LSHIFT";
        break;
    case MOV:
        return "MOV";
        break;
    case NOT:
        return "NOT";
        break;
    default:
        return "UNKNOWN";
    }
    return "UNKOWN";
}

bool is_other(char *token) {
    // OR|AND|LSHIFT|RSHIFT of reg value
    int result;
    char inp1_wire_name[4];
    char inp2_wire_name[4];
    char name[4];
    char op_name[8];

    // REG OP REG
    result = sscanf(token, "%s %s %s -> %s", inp1_wire_name, op_name,
                    inp2_wire_name, name);
    if (result != 4) {
        return false;
    }

    update_wire(get_wire(name), name_to_op(op_name), inp1_wire_name,
                inp2_wire_name);
    return true;
}

bool is_not(char *token) {
    // NOT of reg value
    int result;
    char inp1_wire_name[4];
    char name[4];
    result = sscanf(token, "NOT %s -> %s", inp1_wire_name, name);
    if (result != 2) {
        return false;
    }

    update_wire(get_wire(name), NOT, inp1_wire_name, inp1_wire_name);

    return true;
}

bool is_mov(char *token) {
    // MOV reg|int to reg
    int result;
    char inp1_wire_name[4];
    char name[4];
    result = sscanf(token, "%s -> %s", inp1_wire_name, name);
    if (result != 2) {
        return false;
    }

    update_wire(get_wire(name), MOV, inp1_wire_name, inp1_wire_name);

    return true;
}

int day07() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);

    if (fileContents) {

        const char outer_delimiters[] = "\n";

        char *token;
        char *outer_saveptr = NULL;

        token = strtok_r(fileContents, outer_delimiters, &outer_saveptr);

        while (token != NULL) {

            if ((is_mov(token)) || (is_not(token)) || (is_other(token))) {
                // good
            } else {
                printf("Unknown token: %s\n", token);
            }

            token = strtok_r(NULL, outer_delimiters, &outer_saveptr);
        }

        unsigned short wire_a = get_wire_value(false, get_wire("a"));
        printf("2015 Day 07 Part 1: %hu\n", wire_a);
        char wire_a_value_name[8];
        snprintf(wire_a_value_name, sizeof(wire_a_value_name), "%d", wire_a);
        update_wire(get_wire("b"), MOV, wire_a_value_name, wire_a_value_name);
        wire_a = get_wire_value(true, get_wire("a"));
        printf("2015 Day 07 Part 2: %hu\n", wire_a);

        free(fileContents);

        for (wire_t *wire = wire_head; wire != NULL;) {
            wire_t *wire_temp = wire;
            wire = wire->next;
            free(wire_temp);
        }
    }

    return 0;
}