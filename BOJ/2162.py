# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2162
# Difficulty :    플래티넘V
# Problem :       선분 그룹

# CCW UnionFind

import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3) :
    result = x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2
    return result

def isIntersect(x1, y1, x2, y2, x3, y3, x4, y4) :
    abcCCW = ccw(x1, y1, x2, y2, x3, y3)
    abdCCW = ccw(x1, y1, x2, y2, x4, y4)
    cdaCCW = ccw(x3, y3, x4, y4, x1, y1)
    cdbCCW = ccw(x3, y3, x4, y4, x2, y2)

    if abcCCW*abdCCW > 0 or cdaCCW*cdbCCW > 0 :
        return False
    elif abcCCW*abdCCW == 0 and cdaCCW*cdbCCW == 0 :
        if max(x1, x2) < min(x3, x4) or max(y1, y2) < min(y3, y4) or max(x3, x4) < min(x1, x2) or max(y3, y4) < min(y1, y2) :
            return False
        else :
            return True
    else :
        return True

n = int(input())
parent = [i for i in range(n)]
segment = []

def find(index) :
    if parent[index] == index :
        return index
    parent[index] = find(parent[index])
    return parent[index]

for i in range(n) :
    nowSegment = tuple(map(int, input().split()))
    segment.append(nowSegment)
    for j in range(i) :
        if isIntersect(nowSegment[0], nowSegment[1], nowSegment[2], nowSegment[3], segment[j][0], segment[j][1], segment[j][2], segment[j][3]) :
            parent[find(i)] = find(j)

for i in range(n) :
    parent[i] = find(i)

print(len(set(parent)))
print(parent.count(max(parent, key=parent.count)))