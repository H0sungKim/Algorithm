//
//  main.swift
//  2
//
//  Created by 김호성 on 2024.07.09.
//
// URL :           https://www.acmicpc.net/problem/1546
// Difficulty :    브론즈I
// Problem :       평균

import Foundation

let n: Int = Int(readLine()!)!
let scoreList: [Int] = readLine()!.split(separator: " ").map{ Int($0)! }

var sum: Int = scoreList.reduce(0, +)

print(Double(sum) / Double(n) / Double(scoreList.max()!) * 100)
