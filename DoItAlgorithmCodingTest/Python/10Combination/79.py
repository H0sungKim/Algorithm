# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1010
# Difficulty :    실버V
# Problem :       다리 놓기

# max(a, b) C min(a, b)

for i in range(int(input())) :
    a, b = map(int, input().split())
    
    n = max(a, b)
    k = min(a, b)

    combination = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n+1) :
        combination[i][i] = 1
        combination[i][0] = 1
        combination[i][1] = i

    for i in range(3, n+1) :
        for j in range(i-2) :
            combination[i][j+2] = combination[i-1][j+1] + combination[i-1][j+2]

    print(combination[n][k])