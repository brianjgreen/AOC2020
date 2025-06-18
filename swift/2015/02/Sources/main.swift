// Advent of Code 2015 - Day 2
// 17 June 2025 Brian Green
//
// Problem:
// Part 1: How many total square feet of wrapping paper should they order?
// Part 2: How many total feet of ribbon should they order?
//

import Foundation

do {
    let fileURL = URL(fileURLWithPath: "data.dat")
    let fileContents = try String(contentsOf: fileURL, encoding: .utf8)
    let lines = fileContents.components(separatedBy: .newlines)
    
    var total = 0
    var p2_total: Int = 0
    for package in lines {
        let components = package.split(separator: "x")
        var surface: [Int] = []
        var perimeter: [Int] = []

        guard components.count == 3,
            let length = Int(components[0]),
            let width = Int(components[1]),
            let height = Int(components[2])
        else {
            fatalError("Input is not in the expected format 'IntxIntxInt'")
        }

        surface.append(2 * length * width)
        surface.append(2 * width * height)
        surface.append(2 * height * length)
        total += surface.reduce(0, +) // Use reduce to summ the values
        total += Int((surface.min() ?? 0) / 2)

        perimeter.append((2 * length) + (2 * width))
        perimeter.append((2 * width) + (2 * height))
        perimeter.append((2 * height) + (2 * length))
        p2_total += (length * width * height) + (perimeter.min() ?? 0)
    }

    print("Part 1: \(total)")
    print("Part 2: \(p2_total)")

} catch {
    print("Error reading file: \(error)")
}
