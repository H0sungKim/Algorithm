# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1744
# Difficulty :    골드IV
# Problem :       수 묶기

# Priority Queue

from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
positive = PriorityQueue()
negative = PriorityQueue()
zero = 0
result = 0

for _ in range(n) :
    num = int(input())
    if num == 1 :
        result += 1
    elif num == 0 :
        zero += 1
    elif num > 0 :
        positive.put(num*-1)
    elif num < 0 :
        negative.put(num)

for _ in range(negative.qsize()//2) :
    result += negative.get() * negative.get()

for _ in range(positive.qsize()//2) :
    result += positive.get() * positive.get()

if not negative.empty() :
    if zero == 0 :
        result += negative.get()
    else :
        negative.get()

if not positive.empty() :
    result -= positive.get()

print(result)