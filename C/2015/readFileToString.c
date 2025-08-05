#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INITIAL_BUFFER_SIZE 1024

// Function to read a file and append its contents to a string
char *readFileToString(const char *filename) {
	FILE *file = fopen(filename, "r");
	if (!file) {
		fprintf(stderr, "Could not open file %s for reading.\n",
		        filename);
		return NULL;
	}

	// Initial buffer size
	size_t bufferSize = INITIAL_BUFFER_SIZE;
	char *buffer = malloc(bufferSize);
	if (!buffer) {
		fclose(file);
		fprintf(stderr, "Memory allocation failed.\n");
		return NULL;
	}

	buffer[0] = '\0'; // Initialize buffer as an empty string

	char chunk[1024];
	while (fgets(chunk, sizeof(chunk), file)) {
		size_t chunkLen = strlen(chunk);
		size_t bufferLen = strlen(buffer);

		// Check if we need to resize the buffer
		if (bufferLen + chunkLen + 1 > bufferSize) {
			// Double the buffer size until it 's large enough
			while (bufferLen + chunkLen + 1 > bufferSize) {
				bufferSize *= 2;
			}
			char *temp = realloc(buffer, bufferSize);
			if (!temp) {
				free(buffer);
				fclose(file);
				fprintf(stderr,
				        "Memory reallocation failed.\n");
				return NULL;
			}
			buffer = temp;
		}

		// Append the chunk to the buffer
		strcat(buffer, chunk);
	}

	fclose(file);
	return buffer;
}
