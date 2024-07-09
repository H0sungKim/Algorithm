# 2022 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2164
# Difficulty :    실버IV
# Problem :       카드2

from collections import deque

num = int(input())
card = deque([num - i for i in range(num)])
    
while len(card) != 1 :
    card.pop()
    card.appendleft(card.pop())
    
print(card[0])