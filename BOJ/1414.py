# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1414
# Difficulty :    골드III
# Problem :       불우이웃돕기

# Minimum Spanning Tree

from queue import PriorityQueue
import sys
input = sys.stdin.readline

def getLanLength(char) :
    if 97 <= ord(char) and ord(char) <= 122 :
        return ord(char)-96
    if 65 <= ord(char) and ord(char) <= 90 :
        return ord(char)-38

def find(num) :
    if num == parent[num] :
        return num
    else :
        parent[num] = find(parent[num])
        return parent[num]

n = int(input())
computer = []
lan = PriorityQueue()

for i in range(n) :
    temp = input()
    for j in range(n) :
        if temp[j] == '0' :
            continue
        lan.put((getLanLength(temp[j]), i, j))

useEdge = 0
result = 0
parent = [i for i in range(n)]
lanSum = 0

while lan.qsize() > 0 :
    now = lan.get()
    lanSum += now[0]
    a = find(now[1])
    b = find(now[2])
    if a != b :
        parent[b] = a
        result += now[0]
        useEdge += 1

if useEdge == n-1 :
    print(lanSum-result)
else :
    print("-1")