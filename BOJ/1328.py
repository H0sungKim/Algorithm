# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1328
# Difficulty :    플래티넘V
# Problem :       고층 빌딩

n, l, r = map(int, input().split())

building = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]

building[1][1][1] = 1

for i in range(2, n+1) :
    for j in range(1, i+1) :
        for k in range(1, i+1) :
            building[i][j][k] = (building[i-1][j][k] * (i-2) + building[i-1][j-1][k] + building[i-1][j][k-1]) % 1000000007

print(building[n][l][r])