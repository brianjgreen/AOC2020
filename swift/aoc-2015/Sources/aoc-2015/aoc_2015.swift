// The Swift Programming Language
// https://docs.swift.org/swift-book

import Foundation

func run(day: Int) {
  switch day {
  case 1: Day01.run()
  case 2: Day02.run()
  case 3: Day03.run()
  case 4:
    if #available(macOS 10.15, *) {
      Day04.run()
    } else {
      print("Day 4 requires macOS 10.15 or newer")
    }
  default: print("Day \(day) not implemented.")
  }
}

@main
struct aoc_2015 {
  static func main() {
    let args = CommandLine.arguments
    if args.count > 1, let day = Int(args[1]) {
      run(day: day)
    } else {
      print("Usage: swift run AdventOfCode <day>")
    }
  }
}
