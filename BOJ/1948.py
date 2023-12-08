# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1948
# Difficulty :    플래티넘V
# Problem :       임계경로

from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
m = int(input())
indegree = [0 for _ in range(n)]
city = [[] for _ in range(n)]
reverseCity = [[] for _ in range(n)]
time = [0 for _ in range(n)]
# road = [0 for _ in range(n)]

for _ in range(m) :
    start, end, distance = map(int, input().split())
    city[start-1].append((end-1, distance))
    reverseCity[end-1].append([start-1, distance, True])
    indegree[end-1] += 1

start, end = map(int, input().split())

queue = deque()
queue.append(start-1)

while queue :
    now = queue.pop()
    for i in city[now] :
        indegree[i[0]] -= 1
        if time[now] + i[1] >= time[i[0]] :
            time[i[0]] = time[now] + i[1]
        if indegree[i[0]] == 0 :
            queue.appendleft(i[0])

print(f"{time[end-1]}\n")

queue = deque()
queue.append(end-1)

count = 0
while queue :
    now = queue.pop()
    for i in reverseCity[now] :
        if time[now] == time[i[0]] + i[1] :
            if i[2] :
                count += 1
                i[2] = False
                queue.appendleft(i[0])

print(f"{count}\n")