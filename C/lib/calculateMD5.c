#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "calculateMD5.h"

#if !defined(__APPLE__)
#include <openssl/evp.h>
#endif

void
calculateMD5(const char *input, uint8_t * outputBuffer, char *outputHex)
{
	unsigned char digest[MD5_LEN];
#if defined(__APPLE__)
	CC_MD5(input, (CC_LONG) strlen(input), digest);
#else
	EVP_MD_CTX *mdctx = EVP_MD_CTX_new();
	if (mdctx == NULL) {
		// As a last resort, zero the digest
		memset(digest, 0, MD5_LEN);
	} else {
		unsigned int digest_len = 0;
		if (EVP_DigestInit_ex(mdctx, EVP_md5(), NULL) != 1 ||
			EVP_DigestUpdate(mdctx, input, (size_t) strlen(input)) != 1 ||
			EVP_DigestFinal_ex(mdctx, digest, &digest_len) != 1) {
			memset(digest, 0, MD5_LEN);
		}
		EVP_MD_CTX_free(mdctx);
	}
#endif
	memcpy(outputBuffer, digest, MD5_LEN);
	// Convert the digest to a hexadecimal string
	for (int i = 0; i < MD5_LEN; i++) {
		sprintf(&outputHex[i * 2], "%02x", digest[i]);
	}
	// Null-terminate the string
	outputHex[MD5_LEN * 2] = '\0';
}
