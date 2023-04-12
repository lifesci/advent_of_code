CC = gcc

CFLAGS = -g -Wall

LIB_PATH = ../../../lib/my_c_utils

INCLUDES = -I$(PATH)

default: main

main: main.o
	$(CC) $(CFLAGS) main.o -o main.out

main.o: main.c
	$(CC) $(CFLAGS) -I $(LIB_PATH) -c main.c

clean:
	rm *.o *.out
