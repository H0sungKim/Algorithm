# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1934
# Difficulty :    브론즈I
# Problem :       최소공배수

def getGCD(num1, num2) :
    while num2 :
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1

t = int(input())

for _ in range(t) :
    a, b = map(int, input().split())
    print(a*b//getGCD(a, b))