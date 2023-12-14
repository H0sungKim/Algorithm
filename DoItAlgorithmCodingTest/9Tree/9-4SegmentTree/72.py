# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/10868
# Difficulty :    골드I
# Problem :       최솟값

import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())

treeHeight = 0

temp = n-1
while temp :
    temp //= 2
    treeHeight += 1

treeSize = 2**(treeHeight+1)
tree = [sys.maxsize for _ in range(treeSize)]
leafStart = treeSize//2

for i in range(n) :
    tree[leafStart+i] = int(input())

tempHeight = leafStart//2
for i in range(treeHeight) :
    for j in range(tempHeight) :
        tree[tempHeight+j] = min(tree[(tempHeight+j)*2], tree[(tempHeight+j)*2+1])
    tempHeight //= 2

def getMin(start, end) :
    start = leafStart+start-1
    end = leafStart+end-1
    result = sys.maxsize
    while start <= end :
        if start%2 == 1 :
            result = min(result, tree[start])
            start += 1
        if end%2 == 0 :
            result = min(result, tree[end])
            end -= 1
        start //= 2
        end //= 2
    return result

for _ in range(m) :
    a, b = map(int, input().split())
    print(f"{getMin(a, b)}\n")