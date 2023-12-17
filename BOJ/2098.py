# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2098
# Difficulty :    골드I
# Problem :       외판원 순회

import sys
input = sys.stdin.readline

n = int(input())
w = []

for _ in range(n) :
    w.append(tuple(map(int, input().split())))

dp = [[0 for _ in range(1 << n)] for _ in range(n)]

def traveling(now, visited) :
    if visited == (1 << n) - 1 :
        if w[now][0] != 0 :
            return w[now][0]
        else :
            return float('inf')
    if dp[now][visited] != 0 :
        return dp[now][visited]
    temp = float('inf')
    for i in range(n) :
        if 1 << i & visited == 0 and w[now][i] != 0 :
            temp = min(temp, traveling(i, 2**i | visited) + w[now][i])
    dp[now][visited] = temp
    return temp

print(traveling(0, 1))