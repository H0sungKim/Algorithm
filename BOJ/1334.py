# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1334
# Difficulty :    골드V
# Problem :       다음 팰린드롬 수

# Edit sequentially starting from the lowest digit.

strN = input()

n = int(strN)
result = strN

# When n is a single digit
if len(result) == 1 :
    if n == 9 :
        print(11)
        exit()
    print(n+1)
    exit()

# Edit from after the middle digit to the last digit.
result = result[:len(result)%2+len(result)//2] + result[len(result)//2-1::-1]
if int(result) > n :
    print(result)
    exit()

# Edit the number of middle digits.
temp = str(int(result[:len(result)//2+len(result)%2])+1)
result = temp[:len(result)%2+len(result)//2] + temp[len(result)//2-1::-1]
if len(temp) > len(result)//2 + len(result)%2 :
    result = result[:1] + "0" + result[1:]
print(result)

# TimeOut =====================================
# Keep adding 1 to n until the conditions are satisfied
# 
# n = int(input())
# 
# repeat = True
# while repeat :
#     n += 1
#     temp = str(n)
#     for i in range(len(temp)//2) :
#         if temp[i] != temp[len(temp)-1-i] :
#             repeat = False
#             break
# 
#     repeat = not repeat
# 
# print(n)