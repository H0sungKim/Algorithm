# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11724
# Difficulty :    실버II
# Problem :       연결 요소의 개수

import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

def DFS(index) :
    visited[index] = True
    for i in component[index] :
        if not visited[i] :
            DFS(i)

n, m = map(int, input().split())
component = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(m) :
    a, b = map(int, input().split())
    component[a-1].append(b-1)
    component[b-1].append(a-1)

count = 0
for i in range(n) :
    if not visited[i] :
        count += 1
        DFS(i)

print(count)