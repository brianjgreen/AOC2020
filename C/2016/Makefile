# Source directories
SRC_DIR = .
LIB_DIR = ../lib

# Define the compiler and flags
CC = cc
CFLAGS = -Wall -Wextra -g -I$(LIB_DIR)
LDFLAGS = -lssl -lcrypto -lm -lcjson

# Define the target executable
TARGET = aoc2016

# Source files
SRC_FILES = $(wildcard $(SRC_DIR)/*.c)
LIB_FILES = $(wildcard $(LIB_DIR)/*.c)
SOURCES   = $(SRC_FILES) $(LIB_FILES)

# Define the object files
OBJECTS = $(SOURCES:.c=.o)

# Default target
all: $(TARGET)

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
.PHONY: all clean