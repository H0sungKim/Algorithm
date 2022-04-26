/** Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
 * 
 * Euclid's algorithm
 * 
 * Calculate the greatest common divisor (GCD) of two input integers.
 */

#include <stdio.h>

int getGcd(int num1, int num2) {
    int temp;
    while (num2) {
        temp = num1 % num2;
        num1 = num2;
        num2 = temp;
    }
    return num1;
}

int main() {
    int num1;
    int num2;
    printf("This is a program to calculate the greatest common divisor (GCD) of two input integers.\nEnter the first number : ");
    scanf("%d", &num1);
    printf("Enter the second number : ");
    scanf("%d", &num2);
    printf("\nThe greatest common divisor (GCD) of \e[1;33m%d %d\e[m is \e[1;33m%d\e[m.\n", num1, num2, getGcd(num1, num2));
    return 0;
}