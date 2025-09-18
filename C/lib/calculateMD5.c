#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <CommonCrypto/CommonDigest.h> // Include for MD5 functions

void
calculateMD5(const char *input, uint8_t * outputBuffer, char *outputHex)
{
	unsigned char	digest[CC_MD5_DIGEST_LENGTH];
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
	CC_MD5(input, (CC_LONG) strlen(input), digest);
#pragma clang diagnostic pop
	memcpy(outputBuffer, digest, CC_MD5_DIGEST_LENGTH);
	// Convert the digest to a hexadecimal string
	for (int i = 0; i < CC_MD5_DIGEST_LENGTH; i++) {
		sprintf(&outputHex[i * 2], "%02x", digest[i]);
	}
	// Null - terminate the string
	outputHex[CC_MD5_DIGEST_LENGTH * 2] = '\0';
}
