# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/9251
# Difficulty :    골드V
# Problem :       LCS

a = input()
b = input()

lenA = len(a)
lenB = len(b)

dp = [[0 for _ in range(lenB+1)] for _ in range(lenA+1)]

for i in range(lenA) :
    for j in range(lenB) :
        if a[i] == b[j] :
            dp[i+1][j+1] = dp[i][j] + 1
        else :
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(dp[lenA][lenB])