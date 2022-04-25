/** Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
 * 
 * Calculate Pi (π) using the Wallis product
 */


#include <stdio.h>

int main() {
    int count = 1;
    double pi = 2;
    while (1) {
    // while (count - 1000) {
        pi = pi * 4 * count * count / (2*count-1) / (2*count+1);
        printf("Repeat : %d | %.10lf\n", count, pi);
        count += 1;
    }
    return 0;
}