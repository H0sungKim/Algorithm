# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2251
# Difficulty :    골드V
# Problem :       물통

# Queue

from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

volume = list(map(int, input().split()))

visited = [[False for _ in range(201)] for _ in range(201)]
answer = [False for _ in range(201)]
A = 0
B = 1
C = 2
pourCase = [(A, B), (A, C), (B, A), (B, C), (C, A), (C, B)]

queue = deque()
queue.append((0, 0))
visited[0][0] = True
answer[volume[C]] = True
while queue :
    nowWater = queue.pop()
    nowA = nowWater[A]
    nowB = nowWater[B]
    nowC = volume[C] - nowA - nowB
    for i in range(6) :
        suppose = [nowA, nowB, nowC]
        if suppose[pourCase[i][0]] == 0 :
            continue
        if volume[pourCase[i][1]] - suppose[pourCase[i][1]] < suppose[pourCase[i][0]] :
            suppose[pourCase[i][0]] += suppose[pourCase[i][1]] - volume[pourCase[i][1]]
            suppose[pourCase[i][1]] = volume[pourCase[i][1]]
        else :
            suppose[pourCase[i][1]] += suppose[pourCase[i][0]]
            suppose[pourCase[i][0]] = 0
        if not visited[suppose[A]][suppose[B]] :
            queue.appendleft((suppose[A], suppose[B]))
            visited[suppose[A]][suppose[B]] = True
            if suppose[A] == 0 :
                answer[suppose[C]] = True
            
for i in range(201) :
    if answer[i] :
        print(f"{i} ")
print("\n")