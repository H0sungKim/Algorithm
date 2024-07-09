# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2775
# Difficulty :    브론즈I
# Problem :       부녀회장이 될테야

# k+n C n-1

for i in range(int(input())) :
    tempK = int(input())
    tempN = int(input())
    
    n = tempK+tempN
    k = tempN-1

    combination = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n+1) :
        combination[i][i] = 1
        combination[i][0] = 1
        combination[i][1] = i

    for i in range(3, n+1) :
        for j in range(i-2) :
            combination[i][j+2] = combination[i-1][j+1] + combination[i-1][j+2]

    print(combination[n][k])