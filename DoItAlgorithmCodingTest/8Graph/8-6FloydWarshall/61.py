# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11404
# Difficulty :    골드IV
# Problem :       플로이드

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
distance = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for i in range(n) :
    distance[i][i] = 0

for _ in range(m) :
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if distance[a][b] > c :
        distance[a][b] = c

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if distance[i][j] > distance[i][k] + distance[k][j] :
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(n) :
    for j in range(n) :
        if distance[i][j] == sys.maxsize :
            print("0 ", end="")
        else :
            print(distance[i][j], end=" ")
    print()