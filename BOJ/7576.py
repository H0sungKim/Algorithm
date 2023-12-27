# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/7576
# Difficulty :    골드V
# Problem :       토마토

# BFS

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

tomatos = []
oldQueue = deque()
newQueue = deque()

for _ in range(n) :
    tomatos.append(list(map(int, input().split())))

for i in range(n) :
    for j in range(m) :
        if tomatos[i][j] == 1 :
            oldQueue.append((i, j))

date = 0
while True :
    if not oldQueue :
        break
    while oldQueue :
        now = oldQueue.pop()
        if now[0] > 0 :
            if tomatos[now[0]-1][now[1]] == 0 :
                tomatos[now[0]-1][now[1]] = 1
                newQueue.appendleft((now[0]-1, now[1]))
        if now[0] < n-1 :
            if tomatos[now[0]+1][now[1]] == 0 :
                tomatos[now[0]+1][now[1]] = 1
                newQueue.appendleft((now[0]+1, now[1]))
        if now[1] > 0 :
            if tomatos[now[0]][now[1]-1] == 0 :
                tomatos[now[0]][now[1]-1] = 1
                newQueue.appendleft((now[0], now[1]-1))
        if now[1] < m-1 :
            if tomatos[now[0]][now[1]+1] == 0 :
                tomatos[now[0]][now[1]+1] = 1
                newQueue.appendleft((now[0], now[1]+1))
    date += 1
    oldQueue = newQueue
    newQueue = deque()

for i in range(n) :
    for j in range(m) :
        if tomatos[i][j] == 0 :
            print(-1)
            exit()

print(date-1)