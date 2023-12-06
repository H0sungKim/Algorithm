# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1016
# Difficulty :    골드I
# Problem :       제곱 ㄴㄴ 수

import math

def isPrimeNum(num) :
    sqrtNum = int(math.sqrt(num))
    for i in range(2, sqrtNum+1) :
        if num%i == 0 :
            return False
    return True

minNum, maxNum = map(int, input().split())

number = [False] * (maxNum-minNum+1)

for i in range(2, math.floor(math.sqrt(maxNum))+1) :
    if not isPrimeNum(i) :
        continue
    squareI = i*i
    for j in range(math.ceil(minNum/squareI),math.floor(maxNum/squareI)+1) :
        number[squareI*j-minNum] = True

result = 0
for i in range(maxNum-minNum+1) :
    if number[i] == False :
        result += 1

print(result)