# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11051
# Difficulty :    실버II
# Problem :       이항 계수 2

n, k = map(int, input().split())

combination = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1) :
    combination[i][i] = 1
    combination[i][0] = 1
    combination[i][1] = i

for i in range(3, n+1) :
    for j in range(i-2) :
        combination[i][j+2] = (combination[i-1][j+1] + combination[i-1][j+2]) % 10007

print(combination[n][k])