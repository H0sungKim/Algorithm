# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/16236
# Difficulty :    골드III
# Problem :       아기 상어

# BFS

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
space = []

for _ in range(n) :
    space.append(list(map(int, input().split())))

fish = []
fishCountToGrow = 2
sharkSize = 2

for i in range(n) :
    for j in range(n) :
        if space[i][j] == 9 :
            sharkLocation = (i, j)
            space[i][j] = 0
        elif space[i][j] == 1 :
            fish.append((i, j))

def getMinDistance(sharkSize, sharkLocation, fishLocation) :
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((sharkLocation[0], sharkLocation[1], 0))
    visited[sharkLocation[0]][sharkLocation[1]] = True
    while queue :
        now = queue.pop()
        if now[0] == fishLocation[0] and now[1] == fishLocation[1] :
            return now[2]
        if now[0]-1 >= 0 and space[now[0]-1][now[1]] <= sharkSize and not visited[now[0]-1][now[1]] :
            visited[now[0]-1][now[1]] = True
            queue.appendleft((now[0]-1, now[1], now[2]+1))
        if now[0]+1 <= n-1 and space[now[0]+1][now[1]] <= sharkSize and not visited[now[0]+1][now[1]] :
            visited[now[0]+1][now[1]] = True
            queue.appendleft((now[0]+1, now[1], now[2]+1))
        if now[1]-1 >= 0 and space[now[0]][now[1]-1] <= sharkSize and not visited[now[0]][now[1]-1] :
            visited[now[0]][now[1]-1] = True
            queue.appendleft((now[0], now[1]-1, now[2]+1))
        if now[1]+1 <= n-1 and space[now[0]][now[1]+1] <= sharkSize and not visited[now[0]][now[1]+1] :
            visited[now[0]][now[1]+1] = True
            queue.appendleft((now[0], now[1]+1, now[2]+1))
    return sys.maxsize

time = 0
while len(fish) :

    selectedFishIndex = 0
    minFishDistance = getMinDistance(sharkSize, sharkLocation, fish[0])
    for i in range(1, len(fish)) :
        distance = getMinDistance(sharkSize, sharkLocation, fish[i])
        if distance < minFishDistance :
            minFishDistance = distance
            selectedFishIndex = i
        elif distance == minFishDistance :
            if fish[i][0] < fish[selectedFishIndex][0] :
                minFishDistance = distance
                selectedFishIndex = i
            elif fish[i][0] == fish[selectedFishIndex][0] :
                if fish[i][1] < fish[selectedFishIndex][1] :
                    minFishDistance = distance
                    selectedFishIndex = i

    if minFishDistance == sys.maxsize :
        break

    sharkLocation = fish.pop(selectedFishIndex)
    time += minFishDistance
    fishCountToGrow -= 1
    if fishCountToGrow == 0 :
        sharkSize += 1
        fishCountToGrow = sharkSize
        for i in range(n) :
            for j in range(n) :
                if space[i][j] == sharkSize-1 :
                    fish.append((i, j))

print(time)