#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utils.h"

#define UPPER_OFFSET 38
#define LOWER_OFFSET 96

int char_to_score (char c) {
    if (isupper(c)) {
        return c - UPPER_OFFSET;
    }
    return c - LOWER_OFFSET;
}

int p1 (char *file_name) {
    FILE *fp;
    char *raw_line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen(file_name, "r");
    if (fp == NULL) {
        exit(EXIT_FAILURE);
    }

    int priorities = 0;

    while ((read = getline(&raw_line, &len, fp)) != -1) {
        int len = strlen(raw_line) - 1;
        struct BSTNode *first_half = NULL;
        for (int i = 0; i < len/2; i++) {
            char str[] = {raw_line[i], '\0'};
            bst_insert(&first_half, str, 0);
        }
        for (int i = len/2; i < len; i++) {
            char str[] = {raw_line[i], '\0'};
            if (bst_contains(first_half, str)) {
                int score = char_to_score(raw_line[i]);
                priorities += score;
                break;
            }
        }
        bst_destroy(first_half);
    }

    free(raw_line);
    return priorities;
}

int count_lines(char *file_name) {
    FILE *fp;
    char *raw_line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen(file_name, "r");
    if (fp == NULL) {
        exit(EXIT_FAILURE);
    }

    int lines = 0;

    while ((read = getline(&raw_line, &len, fp)) != -1) {
        lines++;
    }

    free(raw_line);
    return lines;
}

int p2 (char *file_name, int lines) {
    FILE *fp;
    char *raw_line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen(file_name, "r");
    if (fp == NULL) {
        exit(EXIT_FAILURE);
    }

    char groups[lines/3];

    int ind = 0;

    struct BSTNode *group = NULL;
    struct BSTNode *tmp_group = NULL;

    while ((read = getline(&raw_line, &len, fp)) != -1) {
        int len = strlen(raw_line) - 1;

        if (group == NULL) {
            for (int i = 0; i < len; i++) {
                char str[] = {raw_line[i], '\0'};
                bst_insert(&group, str, 0);
            }
        } else {
            for (int i = 0; i < len; i++) {
                char str[] = {raw_line[i], '\0'};
                if (bst_contains(group, str)) {
                    bst_insert(&tmp_group, str, 0);
                }
            }
            group = tmp_group;
            tmp_group = NULL;
        }

        if (ind % 3 == 2) {
            groups[ind/3] = group->key[0];
            bst_destroy(group);
            group = NULL;
        }

        ind++;
    }

    int priorities = 0;
    for (int i = 0; i < lines/3; i++) {
        char c = groups[i];
        priorities += char_to_score(c);
    }

    free(raw_line);
    return priorities;
}

int main () {
    char *input = "input.txt";

    int p1_sol = p1(input);
    printf("%i\n", p1_sol);
    int lines = count_lines(input);
    int p2_sol = p2(input, lines);
    printf("%i\n", p2_sol);
}
