# 2024 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/16724
# Difficulty :    골드III
# Problem :       피리 부는 사나이

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

directions = []
for _ in range(n) :
    for i in input() :
        match i :
            case "U" :
                directions.append(-m)
            case "D" :
                directions.append(+m)
            case "L" :
                directions.append(-1)
            case "R" :
                directions.append(1)

parent = [-1 for _ in range(n*m)]
safeZone = 0
for i in range(n*m) :
    if parent[i] < 0 :
        index = i
        while parent[index] == -1 :
            parent[index] = i
            index += directions[index]
        if i == parent[index] :
            safeZone += 1

print(max(1, safeZone))