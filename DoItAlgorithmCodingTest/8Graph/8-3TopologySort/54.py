# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1516
# Difficulty :    골드III
# Problem :       게임 개발

from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
indegree = [0 for _ in range(n)]
building = [[] for _ in range(n)]
time = []

for i in range(n) :
    temp = list(map(int, input().split()))
    temp.pop()
    time.append(temp.pop(0))
    for j in temp :
        indegree[i] += 1
        building[j-1].append(i)

queue = deque()
for i in range(len(indegree)) :
    if indegree[i] == 0 :
        queue.append(i)

result = time[:]

while queue :
    now = queue.pop()
    for i in building[now] :
        indegree[i] -= 1
        result[i] = max(result[i], time[i] + result[now])
        if indegree[i] == 0 :
            queue.appendleft(i)

for i in result :
    print(f"{i}\n")