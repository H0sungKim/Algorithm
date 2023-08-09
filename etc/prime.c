/** 2022 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
 * 
 * Check the input integer is a prime number.
 */

#include <stdio.h>
#include <math.h>

int isPrimeNum(int num) {
    int sqrtNum = (int) sqrt(num);
    for (int i=2; i<=sqrtNum; i++) {
        if (num%i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int num;
    printf("This is a program that checks whether the input integer is a prime number.\nEnter the number you want to check if it is a prime number. : ");
    scanf("%d", &num);
    if (isPrimeNum(num)) {
        printf("\n\e[1;33m%d\e[m is a prime number.", num);
    } else {
        printf("\n\e[1;33m%d\e[m is \e[1;31mnot\e[m a prime number.", num);
    }
    return 0;
}