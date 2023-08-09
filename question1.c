#include <stdint.h>
#include <stdio.h>

void print_squares(int64_t N, int64_t M) {
    int64_t square_side;

    printf("squares: ");

    // Loops until there is no more paper to cut
    while (N > 0 && M > 0) {

        // Equivalent to cutting the paper, considering the smallest side which
        // will form the square
        if (N < M) {
            square_side = N;
            M -= square_side;
        } else {
            square_side = M;
            N -= square_side;
        }

        printf("%ldx%ld", square_side, square_side);

        // Prints the results aesthetically
        if (N > 0 && M > 0) {
            printf(", ");
        }
    }

    printf("\n");
}

void main() {

    int64_t N, M;

    while (1) {
        printf("insert valid N size: ");
        scanf("%ld", &N);
        printf("insert valid M size: ");
        scanf("%ld", &M);

        // Making sure the inputs are valid within int64_t constraints
        if (N < 1 || M < 1 || N > 9223372036854775806 ||
            M > 9223372036854775806) {
            printf("ERROR: insert a valid size (1 < N, M < "
                   "9223372036854775806)\n");
        } else {
            print_squares(N, M);
            break;
        }
    }
}