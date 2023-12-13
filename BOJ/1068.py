# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1068
# Difficulty :    골드V
# Problem :       트리

# Tree, BFS

from collections import deque

n = int(input())
tree = [[] for _ in range(n)]

temp = list(map(int, input().split()))
for i in range(n) :
    if temp[i] == -1 :
        start = i
        continue
    tree[temp[i]].append(i)

remove = int(input())
queue = deque()
queue.append(start)

leafCount = 0

while queue :
    now = queue.pop()
    if now == remove :
        continue
    if len(tree[now]) == 0 :
        leafCount += 1
    elif len(tree[now]) == 1 :
        if tree[now][0] == remove :
            leafCount += 1
    for i in tree[now] :
        queue.appendleft(i)

print(leafCount)