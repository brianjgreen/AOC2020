#include "calculateMD5.h"
#include "readFileToString.h"
#include <CommonCrypto/CommonDigest.h> // Include for MD5 functions
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATA_FILE "day04.dat"
#define MD5_HASH_HEX_LENGTH (CC_MD5_DIGEST_LENGTH * 2 + 1)

int
day04()
{
	const char     *filename = DATA_FILE;
	char	       *fileContents = readFileToString(filename);
	const char     *five_zeros = "00000";
	const char     *six_zeros = "000000";

	if (fileContents) {
		//printf("%s\n", fileContents);
		//printf("%d", INT_MAX);

		uint8_t		md5_hash[CC_MD5_DIGEST_LENGTH];
		char		md5_hash_hex[MD5_HASH_HEX_LENGTH];
		int		i = 1;
		bool		found_part1 = false;
		bool		found_part2 = false;

		while ((!found_part1) || (!found_part2)) {
			char		input[64];

			snprintf(input, sizeof(input), "%s%d", fileContents, i);
			calculateMD5(input, md5_hash, md5_hash_hex);

			if ((!found_part1) &&
			    (strncmp(md5_hash_hex, five_zeros, strlen(five_zeros)) == 0)) {
				found_part1 = true;
				printf("2015 Day 04 Part 1: %d %s \n", i, md5_hash_hex);
			}
			if ((!found_part2) &&
			    (strncmp(md5_hash_hex, six_zeros, strlen(six_zeros)) == 0)) {
				found_part2 = true;
				printf("2015 Day 04 Part 2: %d %s\n", i, md5_hash_hex);
			}
			i++;
		}

		free(fileContents);
	}

	return 0;
}
