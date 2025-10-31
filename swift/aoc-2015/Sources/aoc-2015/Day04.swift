import Foundation
import CryptoKit

@available(macOS 10.15, *)
enum Day04 {
  
  static func md5Hash(_ string: String) -> String {
    let data = Data(string.utf8)
    let hash = Insecure.MD5.hash(data: data)
    return hash.map { String(format: "%02x", $0) }.joined()
  }
  
  static func findHashWithPrefix(_ key: String, prefix: String, startFrom: Int = 0) -> Int {
    var number = startFrom
    while true {
      let testString = key + String(number)
      let hash = md5Hash(testString)
      if hash.hasPrefix(prefix) {
        return number
      }
      number += 1
    }
  }
  
  static func run() {
    do {
      let fileURL = URL(fileURLWithPath: "../../data/2015/day04.dat")
      let fileContents = try String(contentsOf: fileURL, encoding: .utf8)
      let key = fileContents.trimmingCharacters(in: .whitespacesAndNewlines)
      
      // Part 1: Find lowest number producing MD5 hash starting with "00000"
      let part1Result = findHashWithPrefix(key, prefix: "00000")
      print("Day 4 Part 1: \(part1Result)")
      
      // Part 2: Find lowest number producing MD5 hash starting with "000000"
      // Start from part1Result since any hash with "000000" must also have "00000"
      let part2Result = findHashWithPrefix(key, prefix: "000000", startFrom: part1Result)
      print("Day 4 Part 2: \(part2Result)")
      
    } catch {
      print("Error reading file: \(error)")
    }
  }
}
