# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1377
# Difficulty :    골드II
# Problem :       버블 소트

n = int(input())
num = []

for i in range(n) :
    num.append((int(input()), i))

num.sort()
difMax = 0

for i in range(n) :
    if num[i][1] - i > difMax :
        difMax = num[i][1] - i

print(difMax+1)