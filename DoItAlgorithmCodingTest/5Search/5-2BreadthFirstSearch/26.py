# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1260
# Difficulty :    실버II
# Problem :       DFS와 BFS

from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m, v = map(int, input().split())
num = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(m) :
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    num[a].append(b)
    num[b].append(a)

for i in range(n) :
    num[i].sort()

def DFS(index) :
    print(f"{index+1} ")
    visited[index] = True
    for i in num[index] :
        if not visited[i] :
            DFS(i)

def BFS(index) :
    queue = deque()
    queue.append(index)
    visited[index] = True
    while queue :
        nowNode = queue.pop()
        print(f"{nowNode+1} ")
        for i in num[nowNode] :
            if not visited[i] :
                visited[i] = True
                queue.appendleft(i)

DFS(v-1)
print("\n")
visited = [False for _ in range(n)]
BFS(v-1)