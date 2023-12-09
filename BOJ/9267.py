# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/9267
# Difficulty :    다이아몬드V
# Problem :       A+B

# ax + by = s

# If x and y are both non-negative and their GCD is 1, it is a valid x and y.

def printAnswer(boolean) :
    if boolean :
        print("YES")
    else :
        print("NO")
    exit()
    

def getGCD(num1, num2) :
    while num2 :
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1

a, b, s = map(int,input().split())

# 0 exceptions
if a == 0 and b == 0 :
    printAnswer(s == 0)
elif a == 0 :
    printAnswer(s % b == 0)
elif b == 0 :
    printAnswer(s % a == 0)

gcdAB = getGCD(a, b)

if s % gcdAB != 0 :
    printAnswer(False)

r1 = a
r2 = b
s1 = 1
t1 = 0
s2 = 0
t2 = 1

while r2 :
    share = r1 // r2
    r0 = r1 % r2
    s0 = s1 - share*s2
    t0 = t1 - share*t2
    s1 = s2
    s2 = s0
    t1 = t2
    t2 = t0
    r1 = r2
    r2 = r0

x = s1*s//gcdAB
y = t1*s//gcdAB
x0 = abs(s2)
y0 = abs(t2)


y += (x // x0) * y0
x = x % x0

while y >= 0 :
    if getGCD(x, y) == 1 :
        printAnswer(True)
    x += x0
    y -= y0

printAnswer(False)