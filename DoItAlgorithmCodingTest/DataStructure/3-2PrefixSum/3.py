# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11659
# Difficulty :    실버III
# Problem :       구간 합 구하기 4

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nowSum = 0
prefixSum = [0]

for i in map(int, input().split()) :
    nowSum += i
    prefixSum.append(nowSum)
    
for _ in range(m) :
    i, j = map(int, input().split())
    print(prefixSum[j] - prefixSum[i-1])