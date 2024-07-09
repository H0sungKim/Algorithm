# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11437
# Difficulty :    골드III
# Problem :       LCA

from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
tree = [[] for _ in range(n)]
depth = [0 for _ in range(n)]
parent = [0 for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(n-1) :
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

queue = deque()
queue.append(0)

while queue :
    now = queue.pop()
    visited[now] = True
    for i in tree[now] :
        if not visited[i] :
            depth[i] = depth[now] + 1
            parent[i] = now
            queue.appendleft(i)

def getLCA(index1, index2) :
    if depth[index1] < depth[index2] :
        while depth[index1] != depth[index2] :
            index2 = parent[index2]
    elif depth[index1] > depth[index2] :
        while depth[index1] != depth[index2] :
            index1 = parent[index1]
    while index1 != index2 :
        index1 = parent[index1]
        index2 = parent[index2]
    return index1

m = int(input())
for _ in range(m) :
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(f"{getLCA(a, b)+1}\n")