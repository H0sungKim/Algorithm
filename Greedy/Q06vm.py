# 2022 Hosung.Kim <hyongak516@mail.hongik.ac.kr>

'''
====================
Greedy
Q6. 무지의 먹방 라이브
--------------------
문제 316p
정답 513p
====================
'''

# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3

def solution(food_times, k):
    food = food_times[:]
    t = 0
    while True :
        t += 1
        if k-len(food) < 0 :
            break
        k -= len(food)
        food = [i for i in food if i != t]
    for i in range(len(food_times)) :
        if food_times[i] >= t :
            if k == 0 :
                return i+1
            else :
                k -= 1

# print(solution([3, 1, 2], 3))