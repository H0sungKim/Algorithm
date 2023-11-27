# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/7490
# Difficulty :    골드V
# Problem :       0 만들기

zeroCases = []

def convertNumToStr(num) :
    strNum = str(num)
    result = strNum[0]
    for i in range(1, len(strNum)) :
        result += f" {strNum[i]}"
    return result

def getZeroCase(numList) :
    for i in range(2**(len(numList)-1)) :
        resultSum = numList[0]
        zeroCase = convertNumToStr(numList[0])
        for j in range(len(numList)-1) :
            if i & 2**j == 0 :
                resultSum += numList[j+1]
                zeroCase += "+"
            else :
                resultSum -= numList[j+1]
                zeroCase += "-"
            zeroCase += convertNumToStr(numList[j+1])
        if resultSum == 0 :
            zeroCases.append(zeroCase)

caseNum = int(input())

for k in range(caseNum) :
    zeroCases = []
    n = int(input())
    for i in range(2**(n-1)) :
        temp = "1"
        for j in range(n-1) :
            if i & 2**j == 0 :
                temp += str(j+2)
            else :
                temp += f" {j+2}"
        getZeroCase(list(map(int, temp.split())))
    for i in sorted(zeroCases) :
        print(i)
    print("")