//
//  main.swift
//  3
//
//  Created by 김호성 on 2024.07.10.
//
// URL :           https://www.acmicpc.net/problem/11659
// Difficulty :    실버III
// Problem :       구간 합 구하기 4

import Foundation

let nm: [Int] = readLine()!.split(separator: " ").map{ Int($0)! }

let nums: [Int] = readLine()!.split(separator: " ").map{ Int($0)! }

var nowSum: Int = 0
var prefixSum: [Int] = [0]

for i in nums {
    nowSum += i
    prefixSum.append(nowSum)
}

for _ in 0..<nm[1] {
    let ij: [Int] = readLine()!.split(separator: " ").map{ Int($0)! }
    print(prefixSum[ij[1]] - prefixSum[ij[0]-1])
}
