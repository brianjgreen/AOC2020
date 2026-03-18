# Source directories
SRC_DIR = .
LIB_DIR = ../lib

# Define the compiler and flags
CC = clang
CFLAGS = -Wall -Wextra -g -I$(LIB_DIR)
LDFLAGS = -lm -lssl -lcrypto

# Define the target executable
TARGET = aoc2016

# Source files
SRC_FILES = $(wildcard $(SRC_DIR)/*.c)
LIB_FILES = $(wildcard $(LIB_DIR)/*.c)
SOURCES   = $(SRC_FILES) $(LIB_FILES)

# Define the object files
OBJECTS = $(SOURCES:.c=.o)

# Default target
all: check-openssl $(TARGET)

# Check for OpenSSL headers and libraries
.PHONY: check-openssl
check-openssl:
	@echo "Checking for OpenSSL..."
	@echo "#include <openssl/evp.h>" > /tmp/test_openssl.c
	@echo "int main() { EVP_MD_CTX *ctx = EVP_MD_CTX_new(); EVP_MD_CTX_free(ctx); return 0; }" >> /tmp/test_openssl.c
	@if $(CC) -o /tmp/test_openssl /tmp/test_openssl.c $(LDFLAGS) 2>/dev/null; then \
		echo "OpenSSL found."; \
		rm -f /tmp/test_openssl /tmp/test_openssl.c; \
	else \
		echo "OpenSSL not found. Please install OpenSSL development libraries."; \
		rm -f /tmp/test_openssl /tmp/test_openssl.c; \
		exit 1; \
	fi

# Link the object files to create the executable
$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

# Compile the source files to object files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean the object files and executable
clean:
	rm -f $(OBJECTS) $(TARGET)

# Phony targets
.PHONY: all clean check-openssl