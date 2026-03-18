#include <stdint.h>

#if defined(__APPLE__)
#include <CommonCrypto/CommonDigest.h>
#define MD5_LEN CC_MD5_DIGEST_LENGTH
#else
#include <openssl/md5.h>
#define MD5_LEN MD5_DIGEST_LENGTH
#endif

void calculateMD5(const char *input, uint8_t *outputBuffer, char *outputHex);