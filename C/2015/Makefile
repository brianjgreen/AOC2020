# Define the compiler and flags
CC = cc
CFLAGS = -Wall -Wextra -g
LDFLAGS = -lssl -lcrypto -lm

# Define the target executable
TARGET = aoc2015

# Define the source files
SOURCES = $(wildcard *.c)

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