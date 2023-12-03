# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1940
# Difficulty :    실버IV
# Problem :       주몽

n = int(input())
m = int(input())

material = list(map(int, input().split()))
material.sort()

pointer1 = 0
pointer2 = n-1

result = 0

while pointer1 < pointer2 :
    if m > material[pointer1] + material[pointer2] :
        pointer1 += 1
    elif m < material[pointer1] + material[pointer2] :
        pointer2 -= 1
    else :
        result += 1
        pointer1 += 1
        pointer2 -= 1

print(result)