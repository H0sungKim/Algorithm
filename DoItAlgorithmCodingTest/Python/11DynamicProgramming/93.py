# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2342
# Difficulty :    골드III
# Problem :       Dance Dance Revolution

import sys

instruction = list(map(int, input().split()))

power = [[1, 2, 2, 2, 2], [2, 1, 3, 4, 3], [2, 3, 1, 3, 4], [2, 4, 3, 1, 3], [2, 3, 4, 3, 1]]
dp = [[[sys.maxsize for _ in range(5)] for _ in range(5)] for _ in range(len(instruction))]

dp[0][0][0] = 0

for n in range(len(instruction)-1) :
    for i in range(5) :
        for j in range(5) :
            # left
            dp[n+1][instruction[n]][i] = min(dp[n][j][i] + power[j][instruction[n]], dp[n+1][instruction[n]][i])
            # right
            dp[n+1][i][instruction[n]] = min(dp[n][i][j] + power[j][instruction[n]], dp[n+1][i][instruction[n]])

minPower = sys.maxsize
for i in range(5) :
    for j in range(5) :
        minPower = min(dp[len(instruction)-1][i][j], minPower)

print(minPower)