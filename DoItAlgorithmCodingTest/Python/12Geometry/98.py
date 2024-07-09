# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/17387
# Difficulty :    골드II
# Problem :       선분 교차 2

def ccw(x1, y1, x2, y2, x3, y3) :
    result = x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2
    return result

x1, y1, x2, y2 = tuple(map(int, input().split()))
x3, y3, x4, y4 = tuple(map(int, input().split()))

abcCCW = ccw(x1, y1, x2, y2, x3, y3)
abdCCW = ccw(x1, y1, x2, y2, x4, y4)
cdaCCW = ccw(x3, y3, x4, y4, x1, y1)
cdbCCW = ccw(x3, y3, x4, y4, x2, y2)

if abcCCW*abdCCW > 0 or cdaCCW*cdbCCW > 0 :
    print("0")
elif abcCCW*abdCCW == 0 and cdaCCW*cdbCCW == 0 :
    if max(x1, x2) < min(x3, x4) or max(y1, y2) < min(y3, y4) or max(x3, x4) < min(x1, x2) or max(y3, y4) < min(y1, y2) :
        print("0")
    else :
        print("1")
else :
    print("1")