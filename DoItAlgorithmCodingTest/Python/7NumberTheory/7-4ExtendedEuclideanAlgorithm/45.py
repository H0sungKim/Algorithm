# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/21568
# Difficulty :    채점 불가
# Problem :       Ax+By=C

# 375x + 275y = 375    x=  1, y=  0
# 375x + 275y = 275    x=  0, y=  1
# 375x + 275y = 100    x=  1, y= -1
# 375x + 275y =  75    x= -2, y=  3
# 375x + 275y =  25    x=  3, y= -4

def getGCD(num1, num2) :
    while num2 :
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1

a, b, c = map(int,input().split())

gcdAB = getGCD(a, b)

if c % gcdAB != 0 :
    print("-1")
    exit()

r1 = a
r2 = b
s1 = 1
t1 = 0
s2 = 0
t2 = 1

while r2 :
    share = r1 // r2
    r = r1 % r2
    s = s1 - share*s2
    t = t1 - share*t2
    s1 = s2
    s2 = s
    t1 = t2
    t2 = t
    r1 = r2
    r2 = r

print(s1*c//gcdAB, t1*c//gcdAB)