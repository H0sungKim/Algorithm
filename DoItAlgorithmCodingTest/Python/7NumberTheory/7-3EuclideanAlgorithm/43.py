# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1850
# Difficulty :    실버I
# Problem :       최대공약수

def getGCD(num1, num2) :
    while num2 :
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1

a, b = map(int, input().split())
print("1"*getGCD(a, b))