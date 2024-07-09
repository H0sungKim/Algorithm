# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1931
# Difficulty :    실버I
# Problem :       회의실 배정

import sys
input = sys.stdin.readline

n = int(input())
conference = []

for _ in range(n) :
    start, end = map(int, input().split())
    conference.append([end, start])

conference.sort()

time = 0
count = 0
for i in conference :
    if time <= i[1] :
        time = i[0]
        count += 1

print(count)