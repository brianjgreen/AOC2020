#include "calculateMD5.h"
#include "readFileToString.h"
#include <CommonCrypto/CommonDigest.h> // Include for MD5 functions
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day05.dat"
#define MD5_HASH_HEX_LENGTH (CC_MD5_DIGEST_LENGTH * 2 + 1)

int
day05()
{
	const char     *filename = DATA_FILE;
	char	       *fileContents = readFileToString(filename);
	const char     *five_zeros = "00000";
	char		password_part2[] = {'0', '0', '0', '0', '0', '0', '0', '0'};

	if (fileContents) {

		uint8_t		md5_hash[CC_MD5_DIGEST_LENGTH];
		char		md5_hash_hex[MD5_HASH_HEX_LENGTH];
		int		i = 0;
		int		j = 8;
		int		all_pos_filled = 0;

		printf("2016 Day 05 Part 1: ");
		while ((j > 0) || (all_pos_filled != 0xff)) {
			char		input[64];

			snprintf(input, sizeof(input), "%s%d", fileContents, i);
			calculateMD5(input, md5_hash, md5_hash_hex);

			if (strncmp(md5_hash_hex, five_zeros, strlen(five_zeros)) == 0) {
				if (j > 0) {
					j--;
					printf("%c", md5_hash_hex[5]);
				}

				char		pos = md5_hash_hex[5];
				if ((pos >= '0') && (pos <= '7')) {
					int		p = pos - '0';

					if (((0x01 << p) & all_pos_filled) == 0) {
						all_pos_filled |= 0x01 << p;
						password_part2[p] = md5_hash_hex[6];
					}
				}
			}

			i++;
		}

		printf("\n");
		free(fileContents);
	}

	printf("2016 Day 05 Part 2: ");
	for (int i = 0; i < 8; i++) {
		printf("%c", password_part2[i]);
	}
	printf("\n");

	return 0;
}
