# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2166
# Difficulty :    골드V
# Problem :       다각형의 면적

import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3) :
    result = x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2
    return result

n = int(input())

coordinate = []
for _ in range(n) :
    coordinate.append(tuple(map(int, input().split())))

coordinate.append(coordinate[0])

result = 0
for i in range(n) :
    result += coordinate[i][0]*coordinate[i+1][1] - coordinate[i+1][0]*coordinate[i][1]

print(round(abs(result/2), 1))