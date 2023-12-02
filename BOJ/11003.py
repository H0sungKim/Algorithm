# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11003
# Difficulty :    플래티넘V
# Problem :       최솟값 찾기

# If a number earlier in the order has a larger value, that number can never be chosen as the minimum.

from collections import deque

n, l = map(int, input().split())

num = []

num += list(map(int, input().split()))

sortedNum = deque()
for i in range(n) :

    while sortedNum and sortedNum[len(sortedNum)-1][1] >= num[i] :
        sortedNum.pop()

    sortedNum.append((i, num[i]))

    if sortedNum[0][0] <= i-l :
        sortedNum.popleft()

    print(sortedNum[0][1], end=" ")