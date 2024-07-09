# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11004
# Difficulty :    실버V
# Problem :       K번째 수

import sys
input = sys.stdin.readline

def quickSort(start, end, k) :
    global numList
    if start >= end :
        return
    pivot = partition(start, end)
    if k < pivot :
        quickSort(start, pivot-1, k)
    elif k > pivot :
        quickSort(pivot+1, end, k)
    else :
        return
    
def swap(a, b) :
    global numList
    temp = numList[a]
    numList[a] = numList[b]
    numList[b] = temp

def partition(start, end) :
    global numList

    if start+1 == end :
        if numList[start] > numList[end] :
            swap(start, end)
        return end
    
    middle = (start + end) // 2
    swap(start, middle)
    pivot = numList[start]
    left = start + 1
    right = end
    while left <= right :
        while left <= end and numList[left] < pivot :
            left += 1
        while right >= start and numList[right] > pivot :
            right -= 1
        if left < right :
            swap(left, right)
            left += 1
            right -= 1
        else :
            break
    
    numList[start] = numList[right]
    numList[right] = pivot
    return right

n, k = map(int, input().split())

numList = list(map(int, input().split()))
quickSort(0, n-1, k-1)
print(numList[k-1])