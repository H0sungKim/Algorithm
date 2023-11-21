# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>

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

repeatCount = int(input())

resultTriangle = upgradeTriangle(repeatCount, basicTriangle)

for i in range(len(resultTriangle)) :
    print(resultTriangle[i])