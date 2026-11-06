#include <stdio.h>
#include <stdlib.h>

/* 
 * This function attempts to sum elements of an array.
 * Contains an intentional off-by-one loop error.
 */
int calculate_sum(int *arr, int size) {
    int sum = 0;
    // Bug: loop condition '<= size' causes out-of-bounds access
    for (int i = 0; i <= size; i++) {
        sum += arr[i];
    }
    return sum;
}

int main() {
    int data[] = {1, 2, 3, 4, 5};
    printf("Sum: %d\n", calculate_sum(data, 5));
    return 0;
}
