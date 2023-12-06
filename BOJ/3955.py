# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/3955
# Difficulty :    플래티넘V
# Problem :       캔디 분배

# Extended Euclidean Algorithm

# -k * x + c * answer = 1
# -10 * x + 7 * answer = 1

# -10 * x + 7 * answer =  10    x = -1, answer =  0
# -10 * x + 7 * answer =   7    x =  0, answer =  1
# -10 * x + 7 * answer =   4    x =  1, answer =  2
# -10 * x + 7 * answer =   3    x = -1, answer = -1
# -10 * x + 7 * answer =   1    x =  2, answer =  3

def getGCD(num1, num2) :
    while num2 :
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1

t = int(input())
for _ in range(t) :
    k, c = map(int,input().split())
    # exception
    if c == 1 :
        if k+1 <= 1000000000 :
            print(k+1)
        else :
            print("IMPOSSIBLE")
        continue

    gcdKC = getGCD(k, c)

    if gcdKC != 1 :
        print("IMPOSSIBLE")
        continue

    r1 = k
    r2 = c
    s1 = -1
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

    # exception
    if t1 < 0 :
        t1 += t2
    elif t1 == 0 :
        t1 = abs(t2)
    if t1 <= 1000000000 :
            print(t1)
    else :
        print("IMPOSSIBLE")