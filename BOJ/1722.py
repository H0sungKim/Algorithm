# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1722
# Difficulty :    골드V
# Problem :       순열의 순서

n = int(input())
problem = list(map(int, input().split()))
problemIndex = problem.pop(0)
factorial = []
num = [i+1 for i in range(n)]

temp = 1
for i in range(n-1) :
    temp *= i+1
    factorial.append(temp)

if problemIndex == 1 :
    k = problem.pop()-1
    for i in range(n-1) :
        print(num.pop(k // factorial[n-2-i]), end=" ")
        k %= factorial[n-2-i]
    print(num.pop(), end=" ")
    print()
elif problemIndex == 2 :
    result = 1
    for i in range(n-1) :
        result += num.index(problem[i]) * factorial[n-2-i]
        num.pop(num.index(problem[i]))
    print(result)