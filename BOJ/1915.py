# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1915
# Difficulty :    골드IV
# Problem :       가장 큰 정사각형

n, m = map(int, input().split())

array = [[0 for _ in range(m+1)]]

for i in range(n) :
    array.append([0])
    for j in map(int, list(input())) :
        array[i+1].append(j)

maxSquare = 0
for i in range(1, n+1) :
    for j in range(1, m+1) :
        if array[i][j] == 1 :
            array[i][j] = min(array[i-1][j-1], array[i][j-1], array[i-1][j]) + 1
        if array[i][j] > maxSquare :
            maxSquare = array[i][j]

print(maxSquare*maxSquare)