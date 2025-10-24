import Foundation

enum Day02 {
  static func run() {
    do {
      let fileURL = URL(fileURLWithPath: "../../data/2015/day02.dat")
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
        total += surface.reduce(0, +)  // Use reduce to summ the values
        total += Int((surface.min() ?? 0) / 2)

        perimeter.append((2 * length) + (2 * width))
        perimeter.append((2 * width) + (2 * height))
        perimeter.append((2 * height) + (2 * length))
        p2_total += (length * width * height) + (perimeter.min() ?? 0)
      }

      print("Day 2 Part 1: \(total)")
      print("Day 2 Part 2: \(p2_total)")

    } catch {
      print("Error reading file: \(error)")
    }

  }
}
