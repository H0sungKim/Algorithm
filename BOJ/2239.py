# 2024 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2239
# Difficulty :    골드IV
# Problem :       스도쿠

sudoku = []

for _ in range(9) :
    sudoku.append(list(map(int, list(input()))))

def dfs(depth):
    if depth == 81 :
        for i in sudoku :
            for j in i :
                print(str(j), end="")
            print()
        exit()
    x = depth//9
    y = depth%9
    if sudoku[x][y] == 0 :
        allNum = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        usedNum = set()
        for k in range(9) :
            usedNum.add(sudoku[x][k])
            usedNum.add(sudoku[k][y])
        for k in range(3) :
            for l in range(3) :
                usedNum.add(sudoku[x//3*3+k][y//3*3+l])
        allNum -= usedNum
        for k in list(allNum):
            sudoku[x][y] = k
            dfs(depth+1)
            sudoku[x][y] = 0
    else :
        dfs(depth+1)

dfs(0)