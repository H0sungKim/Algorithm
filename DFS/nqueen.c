#include <stdio.h>
#include <wchar.h>
#include <locale.h>

int mapSize;
int addQueen(int deep, int chess[]);
void printLine(int mapSize, int queen);

int main() {
    setlocale(LC_ALL, "");
    scanf("%d", &mapSize);
    int chess[mapSize];
    printf("%d", addQueen(0, chess));
}

int addQueen(int deep, int chess[]) {
    if (deep == mapSize) {
        // Print Chess Map ==============
        for (int i=0; i<mapSize; i++) {
            printLine(mapSize, chess[i]);
        }
        system("cls");
        // ==============================
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
    for (int i=0; i<queen; i++) {
        wprintf(L"■");
    }
    wprintf(L"□");
    for (int i=0; i<mapSize-queen; i++) {
        wprintf(L"■");
    }
    printf("\n");
}