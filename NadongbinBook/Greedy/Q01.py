# 2022 Hosung.Kim <hyongak516@mail.hongik.ac.kr>

'''
==============
Greedy
Q1. 모험가 길드
--------------
문제 311p
정답 506p
==============
'''

n = int(input())
adventurer = sorted(list(map(int, input().split())))

groupCount = 0
groupMember = 0
for i in adventurer :
    groupMember += 1
    if groupMember >= i :
        groupCount += 1
        groupMember = 0

print(groupCount)