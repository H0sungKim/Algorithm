# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/10026
# Difficulty :    골드V
# Problem :       적록색약

n = int(input())

rgbMap = []
for i in range(n) :
    rgbMap.append(input())

areaMap = [[n*i + j for j in range(n)] for i in range(n)]

flag = 1
while flag == 1 :
    flag = 0
    for i in range(n) :
        for j in range(n) :
            if i-1 >= 0 :
                if rgbMap[i-1][j] == rgbMap[i][j] and areaMap[i-1][j] != areaMap[i][j] :
                    areaMap[i-1][j] = min(areaMap[i-1][j], areaMap[i][j])
                    areaMap[i][j] = min(areaMap[i-1][j], areaMap[i][j])
                    flag = 1
            if j-1 >= 0 :
                if rgbMap[i][j-1] == rgbMap[i][j] and areaMap[i][j-1] != areaMap[i][j] :
                    areaMap[i][j-1] = min(areaMap[i][j-1], areaMap[i][j])
                    areaMap[i][j] = min(areaMap[i][j-1], areaMap[i][j])
                    flag = 1
            if j+1 < n :
                if rgbMap[i][j+1] == rgbMap[i][j] and areaMap[i][j+1] != areaMap[i][j] :
                    areaMap[i][j+1] = min(areaMap[i][j+1], areaMap[i][j])
                    areaMap[i][j] = min(areaMap[i][j+1], areaMap[i][j])
                    flag = 1
            if i+1 < n :
                if rgbMap[i+1][j] == rgbMap[i][j] and areaMap[i+1][j] != areaMap[i][j] :
                    areaMap[i+1][j] = min(areaMap[i+1][j], areaMap[i][j])
                    areaMap[i][j] = min(areaMap[i+1][j], areaMap[i][j])
                    flag = 1

result = set()
for i in range(n) :
    result = result | set(areaMap[i])
# print(areaMap)
print(len(result))

# R82 G71 B66

flag = 1
while flag == 1 :
    flag = 0
    for i in range(n) :
        for j in range(n) :
            if i-1 >= 0 :
                if min(ord(rgbMap[i-1][j]), ord(rgbMap[i][j])) > 70 and areaMap[i-1][j] != areaMap[i][j] :
                    areaMap[i-1][j] = min(areaMap[i-1][j], areaMap[i][j])
                    areaMap[i][j] = min(areaMap[i-1][j], areaMap[i][j])
                    flag = 1
            if j-1 >= 0 :
                if min(ord(rgbMap[i][j-1]), ord(rgbMap[i][j])) > 70 and areaMap[i][j-1] != areaMap[i][j] :
                    areaMap[i][j-1] = min(areaMap[i][j-1], areaMap[i][j])
                    areaMap[i][j] = min(areaMap[i][j-1], areaMap[i][j])
                    flag = 1
            if j+1 < n :
                if min(ord(rgbMap[i][j+1]), ord(rgbMap[i][j])) > 70 and areaMap[i][j+1] != areaMap[i][j] :
                    areaMap[i][j+1] = min(areaMap[i][j+1], areaMap[i][j])
                    areaMap[i][j] = min(areaMap[i][j+1], areaMap[i][j])
                    flag = 1
            if i+1 < n :
                if min(ord(rgbMap[i+1][j]), ord(rgbMap[i][j])) > 70 and areaMap[i+1][j] != areaMap[i][j] :
                    areaMap[i+1][j] = min(areaMap[i+1][j], areaMap[i][j])
                    areaMap[i][j] = min(areaMap[i+1][j], areaMap[i][j])
                    flag = 1

result = set()
for i in range(n) :
    result = result | set(areaMap[i])
# print(areaMap)
print(len(result))