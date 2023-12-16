# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/9252
# Difficulty :    골드IV
# Problem :       LCS 2

# LCS

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

i = lenA
j = lenB

result = []
while i != 0 and j != 0 :
    if a[i-1] == b[j-1] :
        result.append(a[i-1])
        i -= 1
        j -= 1
    else :
        if dp[i-1][j] > dp[i][j-1] :
            i -= 1
        else :
            j -= 1

for i in result[::-1] :
    print(i, end="")