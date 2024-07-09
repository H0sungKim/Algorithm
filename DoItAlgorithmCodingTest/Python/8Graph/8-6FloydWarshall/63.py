# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1389
# Difficulty :    실버I
# Problem :       케빈 베이컨의 6단계 법칙

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
distance = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for i in range(n) :
    distance[i][i] = 0

for _ in range(m) :
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    distance[a][b] = 1
    distance[b][a] = 1

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if distance[i][j] > distance[i][k] + distance[k][j] :
                distance[i][j] = distance[i][k] + distance[k][j]

minK = sys.maxsize
result = -1
for i in range(n) :
    temp = sum(distance[i])
    if minK > temp :
        minK = temp
        result = i

print(result+1)