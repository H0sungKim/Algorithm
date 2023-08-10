/** 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
 * 
 * Calculate the number of divisors.
 */

#include <stdio.h>
#include <math.h>

int countDivisor(int num) {
    const int sqrtNum = (int) sqrt(num);
    int count = 0;
    for (int i=1; i<=sqrtNum; i++) {
        if (num%i == 0) {
            count += 2;
        }
    }
    if (sqrtNum*sqrtNum == num) {
        count -= 1;
    }
    return count;
}

int main() {
    int num;
    char sNum[32];
    char sDivisor[32];
    FILE * file = fopen("test.csv", "w");
    printf("This is a program that calculates the number of divisors up to the input integer.\nEnter the number. : ");
    scanf("%d", &num);

    for (int i=1; i<=num; i++) {
        sprintf(sNum, "%d", i);
        sprintf(sDivisor, "%d", countDivisor(i));
        fputs(sNum, file);
        fputs(",", file);
        fputs(sDivisor, file);
        fputs("\n", file);
        printf("%d :\t %s\n", i, sDivisor);
    }
    fclose(file);

    return 0;
}