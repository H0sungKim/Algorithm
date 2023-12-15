# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/13251
# Difficulty :    실버III
# Problem :       조약돌 꺼내기

m = int(input())
color = list(map(int, input().split()))
k = int(input())

n = sum(color)

combination = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1) :
    combination[i][i] = 1
    combination[i][0] = 1
    combination[i][1] = i

for i in range(3, n+1) :
    for j in range(i-2) :
        combination[i][j+2] = combination[i-1][j+1] + combination[i-1][j+2]

caseSum = 0
for i in color :
    if i < k :
        continue
    caseSum += combination[i][k]

print(caseSum / combination[n][k])