# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2018
# Difficulty :    실버V
# Problem :       수들의 합 5

n = int(input())

result = 1
repeat = 1
while True :
    n -= repeat
    repeat += 1
    if n % repeat == 0 and n > 0 :
        result += 1
    elif n // repeat <= 0 :
        break

print(result)