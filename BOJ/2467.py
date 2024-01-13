# 2024 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2467
# Difficulty :    골드V
# Problem :       용액

# Two Pointer

import sys
input = sys.stdin.readline

n = int(input())

solutions = list(map(int, input().split()))

start = 0
end = n-1

minValue = 9999999999

while start < end :
    dif = solutions[start] + solutions[end]
    if abs(dif) < minValue :
        minValue = abs(dif)
        solution1 = solutions[start]
        solution2 = solutions[end]
    if dif < 0 :
        start += 1
    elif dif > 0 :
        end -= 1
    else :
        print(f"{solution1} {solution2}")
        exit()

print(f"{solution1} {solution2}")