# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1874
# Difficulty :    실버II
# Problem :       스택 수열

from collections import deque

n = int(input())
num = []
for i in range(n) :
    num.append(int(input()))

step = 1
numStack = deque()
result = ""
for i in num :
    if i >= step :
        for j in range(step, i+1) :
            numStack.append(j)
            result += "+"
        numStack.pop()
        result += "-"
        step = i+1
    else :
        if numStack.pop() == i :
            result += "-"
        else :
            print("NO")
            exit()

for i in range(len(result)) :
    print(result[i])