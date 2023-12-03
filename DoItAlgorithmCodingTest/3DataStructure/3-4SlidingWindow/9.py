# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/12891
# Difficulty :    실버II
# Problem :       DNA 비밀번호

s, p = map(int, input().split())
dna = input()
a, c, g, t = map(int, input().split())

tempA = 0
tempC = 0
tempG = 0
tempT = 0

result = 0

for i in range(p) :
    match dna[i] :
        case "A" :
            tempA += 1
        case "C" :
            tempC += 1
        case "G" :
            tempG += 1
        case "T" :
            tempT += 1
if tempA >= a and tempC >= c and tempG >= g and tempT >= t :
    result += 1
for i in range(s-p) :
    match dna[i] :
        case "A" :
            tempA -= 1
        case "C" :
            tempC -= 1
        case "G" :
            tempG -= 1
        case "T" :
            tempT -= 1
    match dna[p+i] :
        case "A" :
            tempA += 1
        case "C" :
            tempC += 1
        case "G" :
            tempG += 1
        case "T" :
            tempT += 1
    if tempA >= a and tempC >= c and tempG >= g and tempT >= t :
        result += 1

print(result)