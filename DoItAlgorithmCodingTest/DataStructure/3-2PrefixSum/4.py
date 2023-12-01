# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11660
# Difficulty :    실버I
# Problem :       구간 합 구하기 5

n, m = map(int, input().split())
table = []

for i in range(n) :
    table.append(list(map(int, input().split())))

prefixTable = [[0 for i in range(n+1)]]
for i in range(n) :
    tempSum = 0
    prefixTable.append([0])
    for j in range(n) :
        tempSum += table[i][j]
        prefixTable[i+1].append(tempSum + prefixTable[i][j+1])

# print(prefixTable)
for i in range(m) :
    x1, y1, x2, y2 = map(int, input().split())
    print(prefixTable[x2][y2] - prefixTable[x2][y1-1] - prefixTable[x1-1][y2] + prefixTable[x1-1][y1-1])