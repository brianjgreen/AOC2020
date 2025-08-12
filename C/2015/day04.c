#include "readFileToString.h"
#include <openssl/evp.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day04.dat"

void generate_md5_hash(const char *input, unsigned char *output) {
    EVP_MD_CTX *mdctx = EVP_MD_CTX_new();
    EVP_DigestInit_ex(mdctx, EVP_md5(), NULL);
    EVP_DigestUpdate(mdctx, input, strlen(input));
    unsigned int len = EVP_MD_size(EVP_md5());
    EVP_DigestFinal_ex(mdctx, output, &len);
    EVP_MD_CTX_free(mdctx);
}

void print_md5_hash(unsigned char *hash) {
    for (int i = 0; i < 16; i++) {
        printf("%02x", hash[i]);
    }
    printf("\n");
}

int day04() {
    const char *filename = DATA_FILE;
    char *fileContents = readFileToString(filename);
    const char *five_zeros = "00000";
    const char *six_zeros = "000000";

    if (fileContents) {
        // printf("%s\n", fileContents);
        // printf("%d", INT_MAX);

        unsigned char md5_hash[16];
        int i = 1;
        bool found_part1 = false;
        bool found_part2 = false;

        while ((!found_part1) || (!found_part2)) {
            char input[64];
            char output[64];

            snprintf(input, sizeof(input), "%s%d", fileContents, i);
            generate_md5_hash(input, md5_hash);
            // printf("%s ", input);
            // print_md5_hash(md5_hash);
            snprintf(output, sizeof(output), "%02x%02x%02x", md5_hash[0],
                     md5_hash[1], md5_hash[2]);
            if ((!found_part1) &&
                (strncmp(output, five_zeros, strlen(five_zeros)) == 0)) {
                found_part1 = true;
                printf("2015 Day 04 Part 1: %d ", i);
                print_md5_hash(md5_hash);
            }
            if ((!found_part2) &&
                (strncmp(output, six_zeros, strlen(six_zeros)) == 0)) {
                found_part2 = true;
                printf("2015 Day 04 Part 2: %d ", i);
                print_md5_hash(md5_hash);
            }
            i++;
        }

        free(fileContents);
    }

    return 0;
}
