# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/14003
# Difficulty :    플래티넘V
# Problem :       가장 긴 증가하는 부분 수열 5

# Longest Increasing Subsequence (LIS)

n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
d = [0, 1]
x = [-float('inf')]
x.append(a[1])
maxLength = 1

def binarySearch(start, end, now) :
    while start < end :
        mid = (start+end)//2
        if x[mid] < now :
            start = mid+1
        else :
            end = mid
    return start

for i in range(n-1) :
    if x[-1] < a[i+2] :
        maxLength += 1
        x.append(a[i+2])
        d.append(maxLength)
    else :
        index = binarySearch(0, len(x)-1, a[i+2])
        x[index] = min(a[i+2], x[index])
        d.append(index)

print(len(x)-1)

find = len(x)-1
answer = []
for i in range(n) :
    if d[n-i] == find :
        answer.append(a[n-i])
        find -= 1
        if find == 0 :
            break

for i in answer[::-1] :
    print(i, end=" ")
print()