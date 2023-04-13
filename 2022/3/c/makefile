CC = gcc

CFLAGS = -g -Wall

LIB_PATH = ../../../lib/my_c_utils

INCLUDES = -I$(PATH)

default: main

main: main.o utils.o
	$(CC) $(CFLAGS) main.o utils.o -o main.out

main.o: main.c
	$(CC) $(CFLAGS) -I $(LIB_PATH) -c main.c

utils.o: $(LIB_PATH)/utils.c
	$(CC) $(CFLAGS) -c $(LIB_PATH)/utils.c

clean:
	rm *.o *.out
