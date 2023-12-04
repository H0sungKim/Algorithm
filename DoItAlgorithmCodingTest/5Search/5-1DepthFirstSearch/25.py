# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/13023
# Difficulty :    골드V
# Problem :       ABCDE

import sys
input = sys.stdin.readline

def DFS(index, depth) :
    if depth == 0 :
        print("1")
        exit()
    visited[index] = True
    depth -= 1
    for i in component[index] :
        if not visited[i] :
            DFS(i, depth)
    visited[index] = False

n, m = map(int, input().split())
component = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(m) :
    a, b = map(int, input().split())
    component[a].append(b)
    component[b].append(a)

for i in range(n) :
    if not visited[i] :
        DFS(i, 4)

print("0")