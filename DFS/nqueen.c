#include <stdio.h>

int mapSize;
int addQueen(int deep, int chess[]);
void printLine(int mapSize, int queen);

int main() {
    
    scanf("%d", &mapSize);
    int chess[mapSize];
    printf("%d", addQueen(0, chess));
}

int addQueen(int deep, int chess[]) {
    if (deep == mapSize) {
        for (int i=0; i<mapSize; i++) {
            printLine(mapSize, chess[i]);
        }
        system("cls");
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

void printLine(int mapSize, int queen) {
    char line[mapSize*2-1];
    for (int i=0; i<sizeof(line); i++) {
        if (i%2 == 1) {
            line[i] = '*';
        } else {
            line[i] = 0;
        }
    }
    line[queen*2] = 'Q';
    for (int i=0; i<sizeof(line); i++) {
        printf("%c", line[i]);
    }
    printf("\n");
}