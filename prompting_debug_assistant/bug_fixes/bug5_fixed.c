#include <stdio.h>
#include <stdlib.h>

/* 
 * This function attempts to sum elements of an array correctly.
 * Fixed loop condition from <= size to < size.
 */
int calculate_sum(int *arr, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

int main() {
    int data[] = {1, 2, 3, 4, 5};
    printf("Sum: %d\n", calculate_sum(data, 5));
    return 0;
}
