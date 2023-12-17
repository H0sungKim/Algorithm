# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11049
# Difficulty :    골드III
# Problem :       행렬 곱셈 순서

import sys

n = int(input())
matrix = []
multiplyCount = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for i in range(n) :
    matrix.append(tuple(map(int, input().split())))
    multiplyCount[i][i] = 0

for i in range(1, n) :
    for j in range(n-i) :
        for k in range(j, i+j) :
            multiplyCount[j][i+j] = min(multiplyCount[j][k] + multiplyCount[k+1][i+j] + matrix[j][0] * matrix[k][1] * matrix[i+j][1], multiplyCount[j][i+j])

print(multiplyCount[0][n-1])