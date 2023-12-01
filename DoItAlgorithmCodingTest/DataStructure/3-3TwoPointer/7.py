# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1940
# Difficulty :    실버IV
# Problem :       주몽

n = int(input())
m = int(input())

material = list(map(int, input().split()))
material.sort()

point1 = 0
point2 = n-1

result = 0

while point1 < point2 :
    if m > material[point1] + material[point2] :
        point1 += 1
    elif m < material[point1] + material[point2] :
        point2 -= 1
    else :
        result += 1
        point1 += 1
        point2 -= 1

print(result)