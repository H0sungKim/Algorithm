# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/10989
# Difficulty :    브론즈I
# Problem :       수 정렬하기 3

import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
num = [0 for _ in range(10001)]

for _ in range(n) :
    num[int(input())] += 1

for i in range(len(num)) :
    for j in range(num[i]) :
        print(f"{i}\n")