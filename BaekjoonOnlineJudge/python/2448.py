# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2448
# Difficulty :    골드IV
# Problem :       별 찍기 - 11

import copy

def upgradeTriangle(repeatCount, triangle) :
    if repeatCount == 0 :
        return triangle
    newTriangle = []
    height = len(triangle)
    for i in range(height) :
        newTriangle.append(" "*height + triangle[i] + " "*height)
    for i in range(height) :
        newTriangle.append(triangle[i] + " " + triangle[i])
        
    return upgradeTriangle(repeatCount-1, newTriangle)
    
basicTriangle = ["  *  ", " * * ", "*****"]

num = int(input())//3
repeatCount = 0

while num != 1 :
    num = num//2
    repeatCount += 1

resultTriangle = upgradeTriangle(repeatCount, basicTriangle)

for i in range(len(resultTriangle)) :
    print(resultTriangle[i])