# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11047
# Difficulty :    실버IV
# Problem :       동전 0

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
count = 0
for _ in range(n) :
    coin.append(int(input()))
for i in range(n) :
    count += k//coin[n-1-i]
    k = k%coin[n-1-i]

print(count)