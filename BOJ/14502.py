# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/14502
# Difficulty :    골드IV
# Problem :       연구소

import copy

def getSafetyZone(virusMap, n, m) :
    flag = 1
    while flag == 1 :
        flag = 0
        for i in range(n) :
            for j in range(m) :
                if virusMap[i][j] == 2 :
                    if i-1 >= 0 :
                        if virusMap[i-1][j] == 0 :
                            virusMap[i-1][j] = 2
                            flag = 1
                    if i+1 < n :
                        if virusMap[i+1][j] == 0 :
                            virusMap[i+1][j] = 2
                            flag = 1
                    if j-1 >= 0 :
                        if virusMap[i][j-1] == 0 :
                            virusMap[i][j-1] = 2
                            flag = 1
                    if j+1 < m :
                        if virusMap[i][j+1] == 0 :
                            virusMap[i][j+1] = 2
                            flag = 1
    safetyZone = 0
    for i in range(n) :
        for j in range(m) :
            if virusMap[i][j] == 0 :
                safetyZone += 1

    return safetyZone

n, m = map(int, input().split())

virusMap = []
mapSize = n * m

for i in range(n) :
    virusMap.append(list(map(int, input().split())))

maxSafetyZone = 0
for i in range(mapSize-2) :
    for j in range(i+1, mapSize-1) :
        for k in range(j+1, mapSize) :
            if virusMap[i//m][i%m] == 0 and virusMap[j//m][j%m] == 0 and virusMap[k//m][k%m] == 0 :
                tempMap = copy.deepcopy(virusMap)
                tempMap[i//m][i%m] = 1
                tempMap[j//m][j%m] = 1
                tempMap[k//m][k%m] = 1
                temp = getSafetyZone(tempMap, n, m)
                if temp > maxSafetyZone :
                    maxSafetyZone = temp
                    # print(tempMap)

print(maxSafetyZone)