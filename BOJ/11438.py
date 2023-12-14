# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11438
# Difficulty :    플래티넘V
# Problem :       LCA 2

# Lowest Common Ancestor

from collections import deque
from math import log2
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
maxDepth = int(log2(n))+1
tree = [[] for _ in range(n)]
depth = [0 for _ in range(n)]
parent = [0 for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(n-1) :
    a, b = map(int, input().split())
    tree[a-1].append(b)
    tree[b-1].append(a)

queue = deque()
queue.append(1)
while queue :
    now = queue.pop()
    visited[now-1] = True
    for i in tree[now-1] :
        if not visited[i-1] :
            depth[i-1] = depth[now-1] + 1
            parent[i-1] = now
            queue.appendleft(i)

extendedParent = [[0 for _ in range(maxDepth)] for _ in range(n)]
for i in range(n) :
    extendedParent[i][0] = parent[i]

for i in range(1, maxDepth) :
    for j in range(n) :
        extendedParent[j][i] = extendedParent[max(0, extendedParent[j][i-1]-1)][i-1]

def getLCA(index1, index2) :
    if depth[index2] > depth[index1]  :
        index1, index2 = index2, index1
    for i in range(maxDepth) :
        if 2**(maxDepth-i-1) <= depth[index1] - depth[index2] :
            if depth[index2] <= depth[extendedParent[index1][maxDepth-i-1]-1] :
                index1 = extendedParent[index1][maxDepth-i-1]-1
    if index1 == index2 :
        return index1+1
    for i in range(maxDepth) :
        if extendedParent[index1][maxDepth-i-1] != extendedParent[index2][maxDepth-i-1] :
            index1 = extendedParent[index1][maxDepth-i-1]-1
            index2 = extendedParent[index2][maxDepth-i-1]-1
    return extendedParent[index1][0]
    

m = int(input())
for _ in range(m) :
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(f"{getLCA(a, b)}\n")