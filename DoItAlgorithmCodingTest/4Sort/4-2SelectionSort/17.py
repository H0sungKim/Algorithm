# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1427
# Difficulty :    실버V
# Problem :       소트인사이드

n = input()

digitN = []

for i in range(len(n)) :
    digitN.append(int(n[i]))

for i in range(len(n)) :
    maxDigit = i
    for j in range(i+1, len(n)) :
        if digitN[j] > digitN[maxDigit] :
            maxDigit = j
    temp = digitN[i]
    digitN[i] = digitN[maxDigit]
    digitN[maxDigit] = temp
    
for i in digitN :
    print(i,end="")
print()