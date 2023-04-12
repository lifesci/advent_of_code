#include <stdio.h>
#include <stdlib.h>

#define OPP_ROCK 'A'
#define OPP_PAPER 'B'
#define OPP_SCISSORS 'C'

#define ROCK 'X'
#define PAPER 'Y'
#define SCISSORS 'Z'

#define ROCK_INT 0
#define PAPER_INT 1
#define SCISSORS_INT 2

#define OPP_MOVE 0
#define MOVE 2

#define WIN_SCORE 6
#define DRAW_SCORE 3
#define LOSS_SCORE 0

#define LOSS 'X'
#define DRAW 'Y'
#define WIN 'Z'

int move_to_int (char move) {
    int out;
    if (move == ROCK || move == OPP_ROCK) {
        out = ROCK_INT;
    }
    else if (move == PAPER || move == OPP_PAPER) {
        out = PAPER_INT;
    }
    else if (move == SCISSORS || move == OPP_SCISSORS) {
        out = SCISSORS_INT;
    }
    return out;
}

int move_to_score (int move) {
    return move + 1;
}

int p1 (char *file_name) {
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen(file_name, "r");
    if (fp == NULL) {
        exit(EXIT_FAILURE);
    }

    int score = 0;

    while ((read = getline(&line, &len, fp)) != -1) {
        int opp_move = move_to_int(line[OPP_MOVE]);
        int move = move_to_int(line[MOVE]);
        score += move_to_score(move);
        if (move == opp_move) {
            score += DRAW_SCORE;
        } else if (move == (opp_move + 1) % 3) {
            score += WIN_SCORE;
        } else {
            score += LOSS_SCORE;
        }
    }

    free(line);
    return score;
}

int p2 (char *file_name) {
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen(file_name, "r");
    if (fp == NULL) {
        exit(EXIT_FAILURE);
    }

    int score = 0;

    while ((read = getline(&line, &len, fp)) != -1) {
        int opp_move = move_to_int(line[OPP_MOVE]);
        char outcome = line[MOVE];
        int move;
        if (outcome == WIN) {
            move = (opp_move + 1) % 3;
            score += WIN_SCORE;
        } else if (outcome == DRAW) {
            move = opp_move;
            score += DRAW_SCORE;
        } else if (outcome == LOSS) {
            move = (opp_move + 2) % 3;
            score += LOSS_SCORE;
        }
        score += move_to_score(move);
    }

    free(line);
    return score;
}

int main () {
    char *input = "input.txt";

    int p1_score = p1(input);
    printf("%i\n", p1_score);

    int p2_score = p2(input);
    printf("%i\n", p2_score);
}
