/**
 * 2022 Hosung.Kim <hyongakt516@mail.hongik.ac.kr>
 * 
 * URL :        https://www.acmicpc.net/problem/9663
 * Difficulty : 골드IV
 * Problem :    N-Queen
 * 
*/

#include <stdio.h>

int mapSize;
int addQueen(int deep, int chess[]);

int main() {
    
    scanf("%d", &mapSize);
    int chess[mapSize];
    printf("%d", addQueen(0, chess));
}

int addQueen(int deep, int chess[]) {
    if (deep == mapSize) {
        return 1;
    }
    int result = 0;
    int flag;

    for (int i=0; i<mapSize; i++) {
        flag = 0;
        for (int j=0; j<deep; j++) {
            if (chess[j] == i || j+chess[j] == deep+i || j-chess[j] == deep-i) {
                flag = 1;
                break;
            }
        }
        if (flag == 0) {
            chess[deep] = i;
            result += addQueen(deep + 1, chess);
        }
    }
    return result;
}