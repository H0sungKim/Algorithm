# 2024 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1799
# Difficulty :    골드I
# Problem :       비숍

# DFS

import sys
input = sys.stdin.readline

n = int(input())

chessBoard = []
for _ in range(n) :
    chessBoard.append(list(map(int, input().split())))
valid = [[[] for _ in range(n)], [[] for _ in range(n-1)]]
for i in range(n) :
    for j in range(n) :
        if chessBoard[i][j] == 1 :
            valid[(i+j)%2][(i+j)//2].append((i, j))
            
def dfs(color, depth, remained, bishop) :
    if depth == 0 and remained == 0 :
        return True
    for i in valid[color][n-depth-color] :
        bitmask = 2**((i[0]-i[1]+n-1)//2)
        if bishop & bitmask == 0 :
            if dfs(color, depth-1, remained-1, bishop | bitmask) :
                return True
    if depth > remained :
        if dfs(color, depth-1, remained, bishop) :
            return True
    return False

WHITE = 0
BLACK = 1

whiteBishop = n
for i in range(n) :
    if dfs(WHITE, n, whiteBishop, 0) :
        break
    whiteBishop -= 1

blackBishop = n-1
for i in range(n-1) :
    if dfs(BLACK, n-1, blackBishop, 0) :
        break
    blackBishop -= 1

print(whiteBishop+blackBishop)