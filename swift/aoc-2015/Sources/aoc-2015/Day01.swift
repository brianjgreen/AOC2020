import Foundation

enum Day01 {
  static func run() {
    do {
      let fileURL = URL(fileURLWithPath: "../../data/2015/day01.dat")
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
          print("Day01 Part 2: BASEMENT pos=\(position)")
        }
      }
      print("Day01 Part 1 = \(floor)")

    } catch {
      print("Error reading file: \(error)")
    }

  }
}
