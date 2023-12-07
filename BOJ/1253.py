# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1253
# Difficulty :    골드IV
# Problem :       좋다

# Two Pointer

n = int(input())

num = list(map(int, input().split()))
num.sort()

result = 0
for i in range(n) :
    pointer1 = 0
    pointer2 = n-1
    while pointer1 < pointer2 :
        if num[i] > num[pointer1] + num[pointer2] :
            pointer1 += 1
        elif num[i] < num[pointer1] + num[pointer2] :
            pointer2 -= 1
        else :
            if pointer1 == i :
                pointer1 += 1
            elif pointer2 == i :
                pointer2 -= 1
            else :
                result += 1
                break

print(result)