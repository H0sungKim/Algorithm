# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1715
# Difficulty :    골드IV
# Problem :       카드 정렬하기

# Priority Queue

from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
card = PriorityQueue()

for _ in range(n) :
    card.put(int(input()))

count = 0
for _ in range(n-1) :
    temp = card.get() + card.get()
    count += temp
    card.put(temp)

print(count)