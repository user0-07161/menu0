CLEAN_FILES = main.c menu0
SRC_FILES = main.c
OUTPUT = menu0
CC = gcc
CFLAGS = -O2 -fno-exceptions

all: build $(OUTPUT)
$(OUTPUT): $(SRC_FILES)
	$(CC) $(CFLAGS) -o $(OUTPUT) $(SRC_FILES)
build:
	cython main.py
clean:
	rm -rf $(CLEAN_FILES)
