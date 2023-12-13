# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1991
# Difficulty :    실버I
# Problem :       트리 순회

import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
tree = [0 for _ in range(n)]

for i in range(n) :
    parent, left, right = input().split()
    tree[ord(parent)-65] = (left, right)

def preorderTraversal(node) :
    if node == '.' :
        return
    print(node)
    index = ord(node)-65
    preorderTraversal(tree[index][0])
    preorderTraversal(tree[index][1])

def inorderTraversal(node) :
    if node == '.' :
        return
    index = ord(node)-65
    inorderTraversal(tree[index][0])
    print(node)
    inorderTraversal(tree[index][1])

def postorderTraversal(node) :
    if node == '.' :
        return
    index = ord(node)-65
    postorderTraversal(tree[index][0])
    postorderTraversal(tree[index][1])
    print(node)

preorderTraversal('A')
print("\n")
inorderTraversal('A')
print("\n")
postorderTraversal('A')
print("\n")