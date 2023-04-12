#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int count_elves (char *file_name) {
    int elves = 1;
    FILE *fp;
    char *raw_line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen(file_name, "r");
    if (fp == NULL) {
        exit(EXIT_FAILURE);
    }

    while ((read = getline(&raw_line, &len, fp)) != -1) {
        if (atoi(raw_line) == 0) {
            elves++;
        }
    }

    free(raw_line);
    return elves;
}

void get_totals (char *file_name, int *totals) {
    FILE *fp;
    char *raw_line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen(file_name, "r");
    if (fp == NULL) {
        exit(EXIT_FAILURE);
    }

    int elf_ind = 0;
    totals[elf_ind] = 0;
    while ((read = getline(&raw_line, &len, fp)) != -1) {
        if (atoi(raw_line) > 0) {
            totals[elf_ind] += atoi(raw_line);
        } else {
            elf_ind++;
            totals[elf_ind] = 0;
        }
    }

    free(raw_line);
}

void merge(int *arr, int l, int r) {
    int tmp_arr[r - l];
    int mid = (r + l)/2;
    int l_ind = l;
    int r_ind = mid;
    for (int i = l; i < r; i++) {
        if (l_ind >= mid) {
            tmp_arr[i - l] = arr[r_ind];
            r_ind++;
        } else if (r_ind >= r) {
            tmp_arr[i - l] = arr[l_ind];
            l_ind++;
        } else {
            if (arr[l_ind] <= arr[r_ind]) {
                tmp_arr[i - l] = arr[l_ind];
                l_ind++;
            } else {
                tmp_arr[i - l] = arr[r_ind];
                r_ind++;
            }
        }
    }

    for (int i = l; i < r; i++) {
        arr[i] = tmp_arr[i - l];
    }
}

void mergesort (int *arr, int l, int r) {
    if ((r - l) <= 1) return;
    int mid = (r + l)/2;
    mergesort(arr, l, mid);
    mergesort(arr, mid, r);
    merge(arr, l, r);
}

int top_n (int n, int *vals, int len) {
    int copy[len];
    for (int i = 0; i < len; i++) {
        copy[i] = vals[i];
    }
    mergesort(copy, 0, len);
    int adj_n = n <= len ? n : len;
    int total = 0;
    for(int i = 0; i < n; i++) {
        total += copy[len - i - 1];
    }
    return total;
}

int main () {
    char *input = "input.txt";
    int elf_count = count_elves(input);
    int totals[elf_count];
    get_totals(input, totals);

    int p1_total = top_n(1, totals, elf_count);
    printf("%i\n", p1_total);

    int p2_total = top_n(3, totals, elf_count);
    printf("%i\n", p2_total);
}
