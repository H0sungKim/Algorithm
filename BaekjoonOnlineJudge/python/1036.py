# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1036
# Difficulty :    골드I
# Problem :       36진수

import copy

inputCount = int(input())
number = []
radix = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
maxLength = 0
for i in range(inputCount) :
    inputNum = input()
    number.append(list(inputNum[::-1]))
  
zNum = int(input())
alphabetExchangeSum = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}
for i in alphabetExchangeSum.keys() :
    tempSum = 0
    tempNumber = copy.deepcopy(number)
    for j in range(len(number)) :
        for k in range(len(number[j])) :
            if tempNumber[j][k] == i :
                tempNumber[j][k] = "Z"
            tempSum += 36**k * radix.index(tempNumber[j][k])
    alphabetExchangeSum[i] = tempSum

sortedAlphabet = sorted(alphabetExchangeSum.items(), key = lambda item: item[1], reverse = True)
sortedAlphabet = sortedAlphabet[:zNum]

for i in sortedAlphabet :
    for j in range(len(number)) :
        for k in range(len(number[j])) :
            if number[j][k] == i[0] :
                number[j][k] = "Z"

numberSum = 0
for i in range(len(number)) :
    for j in range(len(number[i])) :
        numberSum += 36**j * radix.index(number[i][j])

resultSum = ""
share = numberSum // 36
remainder = numberSum % 36
while share>=36 :
    resultSum += radix[remainder]
    remainder = share % 36
    share = share // 36
resultSum += radix[remainder]
if share != 0 :
    resultSum += radix[share]

print(resultSum[::-1])