# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11689
# Difficulty :    골드I
# Problem :       GCD(n, k) = 1

# Euler's totient function
# ==============================
# Euler's totient function counts the positive integers up to a given integer n that are relatively prime to n.
# 20 = 2**2 + 5
# 20 * (1-1/2) * (1-1/5)

num = int(input())
result = num
for i in range(2, int(num ** 0.5)+1) :
    if num % i == 0 :
        while num%i == 0 :
            num //= i
        result -= result // i

if num > 1 :
    result -= result // num

print(result)