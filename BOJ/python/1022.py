# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1022
# Difficulty :    골드III
# Problem :       소용돌이 예쁘게 출력하기

def getValue(r, c) :
    step = max(abs(r), abs(c))
    height = 2*step + 1
    if r == step :
        return height**2 - step + c
    elif c == -1 * step :
        return height**2 - step*3 + r
    elif r == -1 * step :
        return height**2 - step*5 - c
    elif c == step :
        return height**2 - step*7 - r


r1 , c1, r2, c2 = map(int, input().split())

maxLength = len(str(max(getValue(r1, c1), getValue(r2, c1), getValue(r1, c2), getValue(r2, c2))))+1

for r in range(r1, r2+1) :
    for c in range(c1, c2+1) :
        if c == c1 :
            print(str(getValue(r, c)).rjust(maxLength-1," "),end="")
        else :
            print(str(getValue(r, c)).rjust(maxLength," "),end="")
    print("")