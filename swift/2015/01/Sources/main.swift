// Advent of Code 2015 - Day 1
// 17 June 2025 Brian Green
//
// Problem:
// Part 1: To what floor do the instructions take Santa?
// Part 2: What is the position of the character that causes Santa to first enter the basement?
//

import Foundation

do {
    let fileURL = URL(fileURLWithPath: "data.dat")
    let fileContents = try String(contentsOf: fileURL, encoding: .utf8)
    
    var floor = 0
    var position = 0
    var found = false
    for char in fileContents {
        position += 1
        if char == ")" {
            floor -= 1
        } else {
            floor += 1
        }

        // First time entering the basement (part 2)
        if !found && floor == -1 {
            found = true
            print("Part 2: BASEMENT pos=\(position)")
        }
    }
    print("Part 1 = \(floor)")

} catch {
    print("Error reading file: \(error)")
}
