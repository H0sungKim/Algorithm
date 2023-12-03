# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/17298
# Difficulty :    골드IV
# Problem :       오큰수

n = int(input())
num = list(map(int, input().split()))

numStack = []

# If there is a larger number on the right, pop the index number and store the larger number there.
for i in range(n) :
    while numStack and num[i] > num[numStack[-1]] :
        num[numStack.pop()] = num[i]
    numStack.append(i)
# unpoped elements are -1.
for i in numStack :
    num[i] = -1

for i in num :
    print(i, end=" ")
print()