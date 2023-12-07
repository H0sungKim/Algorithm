# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1517
# Difficulty :    플래티넘V
# Problem :       버블 소트

# Merge Sort

import sys
input = sys.stdin.readline

def mergeSort(lst) :
    global result
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
            result += mid-leftPoint
            lst.append(right[rightPoint])
            rightPoint += 1

    lst.extend(left[leftPoint:])
    lst.extend(right[rightPoint:])


n = int(input())

num = list(map(int, input().split()))
result = 0

mergeSort(num)

print(result)