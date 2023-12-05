# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2178
# Difficulty :    실버I
# Problem :       미로 탐색

from collections import deque

n, m = map(int, input().split())

maze = [[] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n) :
    for j in input() :
        maze[i].append(int(j))

def BFS(x, y) :
    queue = deque()
    queue.append((x, y, 1))
    visited[x][y] = True
    while queue :
        nowNode = queue.pop()
        if nowNode[0] == n-1 and nowNode[1] == m-1 :
            print(nowNode[2])
            exit()

        if nowNode[0]-1 >= 0 and maze[nowNode[0]-1][nowNode[1]] and not visited[nowNode[0]-1][nowNode[1]] :
            visited[nowNode[0]-1][nowNode[1]] = True
            queue.appendleft((nowNode[0]-1, nowNode[1], nowNode[2]+1))

        if nowNode[1]-1 >= 0 and maze[nowNode[0]][nowNode[1]-1] and not visited[nowNode[0]][nowNode[1]-1] :
            visited[nowNode[0]][nowNode[1]-1] = True
            queue.appendleft((nowNode[0], nowNode[1]-1, nowNode[2]+1))

        if nowNode[0]+1 < n and maze[nowNode[0]+1][nowNode[1]] and not visited[nowNode[0]+1][nowNode[1]] :
            visited[nowNode[0]+1][nowNode[1]] = True
            queue.appendleft((nowNode[0]+1, nowNode[1], nowNode[2]+1))

        if nowNode[1]+1 < m and maze[nowNode[0]][nowNode[1]+1] and not visited[nowNode[0]][nowNode[1]+1] :
            visited[nowNode[0]][nowNode[1]+1] = True
            queue.appendleft((nowNode[0], nowNode[1]+1, nowNode[2]+1))

BFS(0, 0)