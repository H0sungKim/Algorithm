# 2022 Hosung.Kim <hyongak516@mail.hongik.ac.kr>

'''
====================
Implementation
Q7. 럭키 스트레이트
--------------------
문제 321p
정답 515p
====================
'''

n = input()
length = len(n)
scoreSum = 0

for i in range(length//2) :
    scoreSum += int(n[i])

for i in range(length//2, length) :
    scoreSum -= int(n[i])

if scoreSum == 0 :
    print("LUCKY")
else :
    print("READY")