# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1920
# Difficulty :    실버IV
# Problem :       수 찾기

n = int(input())
num = list(map(int, input().split()))
num.sort()

m = int(input())
searchList = list(map(int, input().split()))

for i in searchList :
    start = 0
    end = n-1
    notFound = True
    while start <= end :
        mid = (start+end)//2
        if i > num[mid] :
            start = mid+1
        elif i < num[mid] :
            end = mid-1
        else :
            print("1")
            notFound = False
            break
    if notFound :
        print("0")