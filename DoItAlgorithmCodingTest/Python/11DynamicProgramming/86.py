# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2193
# Difficulty :    실버III
# Problem :       이친수

n = int(input())

pinary = (0, 1)

for i in range(n-1) :
    num0 = pinary[0] + pinary[1]
    num1 = pinary[0]
    pinary = (num0, num1)

print(pinary[0] + pinary[1])