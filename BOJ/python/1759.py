# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1759
# Difficulty :    골드V
# Problem :       암호 만들기

import re

def printPassword(password, letter, depth) :
    if depth == 0 :
        vowel = 0
        for i in password :
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
                vowel += 1
        if vowel > 0 and len(password)-vowel >= 2 :
            print(password)
    for i in letter :
        if len(password) == 0 or ord(password[-1]) < ord(i) :
            newLetter = re.sub(i, '', letter)
            printPassword(password+i, newLetter, depth-1)
        

l, c = map(int, input().split())

letter = input().split()
letter.sort()
letter = "".join(letter)

printPassword("", letter, l)