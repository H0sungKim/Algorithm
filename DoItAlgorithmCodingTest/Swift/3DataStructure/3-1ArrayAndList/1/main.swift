//
//  main.swift
//  1
//
//  Created by 김호성 on 2024.07.09.
//
// URL :           https://www.acmicpc.net/problem/11720
// Difficulty :    브론즈IV
// Problem :       숫자의 합

import Foundation

let n: Int = Int(readLine()!)!
let numList: [Character] = Array(readLine()!)
var numSum = 0

for i in 0..<n {
    numSum += Int(String(numList[i]))!
}

print(numSum)
