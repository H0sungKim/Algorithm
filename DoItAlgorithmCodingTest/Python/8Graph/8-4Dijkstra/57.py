# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1916
# Difficulty :    골드V
# Problem :       최소비용 구하기

from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

bus = [[] for _ in range(n)]
visited = [False for _ in range(n)]
price = [sys.maxsize for _ in range(n)]

for _ in range(m) :
    start, end, busPrice = map(int, input().split())
    bus[start-1].append((busPrice, end-1))

start, end = map(int, input().split())

queue = PriorityQueue()
queue.put((0, start-1))
price[start-1] = 0

while queue.qsize() > 0 :
    now = queue.get()
    if visited[now[1]] :
        continue
    visited[now[1]] = True
    for i in bus[now[1]] :
        if price[i[1]] > price[now[1]] + i[0] :
            price[i[1]] = price[now[1]] + i[0]
            queue.put((price[i[1]], i[1]))

print(price[end-1])