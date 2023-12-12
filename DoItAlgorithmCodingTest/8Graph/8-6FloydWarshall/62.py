# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11403
# Difficulty :    실버I
# Problem :       경로 찾기

import sys
input = sys.stdin.readline

n = int(input())
distance = []

for _ in range(n) :
    distance.append(list(map(int, input().split())))

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if distance[i][k] == 1 and distance[k][j] == 1 :
                distance[i][j] = 1

for i in range(n) :
    for j in range(n) :
        print(distance[i][j], end=" ")
    print()