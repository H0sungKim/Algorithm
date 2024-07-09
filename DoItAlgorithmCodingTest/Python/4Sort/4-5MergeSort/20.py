# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2751
# Difficulty :    실버V
# Problem :       수 정렬하기 2

import sys
input = sys.stdin.readline
print = sys.stdout.write

def mergeSort(lst) :
    mid = len(lst) // 2

    left = lst[:mid]
    right = lst[mid:]
    lst[:] = []

    leftLen = len(left)
    rightLen = len(right)

    if leftLen > 1 :
        mergeSort(left)
    if rightLen > 1 :
        mergeSort(right)

    leftPoint = 0
    rightPoint = 0

    while leftPoint < leftLen and rightPoint < rightLen :
        if left[leftPoint] <= right[rightPoint] :
            lst.append(left[leftPoint])
            leftPoint += 1
        else :
            lst.append(right[rightPoint])
            rightPoint += 1

    lst.extend(left[leftPoint:])
    lst.extend(right[rightPoint:])


n = int(input())

num = []

for i in range(n) :
    num.append(int(input()))

mergeSort(num)

for i in num :
    print(f"{i}\n")