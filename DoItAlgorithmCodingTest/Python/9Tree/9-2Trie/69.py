# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/14425
# Difficulty :    실버IV
# Problem :       문자열 집합

import sys
input = sys.stdin.readline

class Node() :
    def __init__(self) :
        self.children = {}

class Trie() :
    def __init__(self) :
        self.head = Node()

    def insert(self, string) :
        nowNode = self.head
        for char in string :
            if char not in nowNode.children :
                nowNode.children[char] = Node()
            nowNode = nowNode.children[char]
    
    def search(self, string) :
        nowNode = self.head
        for char in string :
            if char in nowNode.children :
                nowNode = nowNode.children[char]
            else :
                return False
        return True
    
trie = Trie()
n, m = map(int, input().split())

for _ in range(n) :
    trie.insert(input())

answer = 0
for _ in range(m) :
    if trie.search(input()) :
        answer += 1

print(answer)