# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11286
# Difficulty :    실버I
# Problem :       절댓값 힙

from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
absQueue = PriorityQueue()

for i in range(n) :
    request = int(input())
    if request == 0 :
        if absQueue.empty() :
            print("0\n")
        else :
            print(str(absQueue.get()[1])+"\n")
    else :
        absQueue.put((abs(request), request))