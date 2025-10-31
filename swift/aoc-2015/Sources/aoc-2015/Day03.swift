import Foundation

enum Day03 {
  // Struct to represent a coordinate that can be used as a dictionary key
  struct Coord: Hashable {
    let x: Int
    let y: Int
  }
  
  static func run() {
    do {
      let fileURL = URL(fileURLWithPath: "../../data/2015/day03.dat")
      let fileContents = try String(contentsOf: fileURL, encoding: .utf8)
      let directions = fileContents.trimmingCharacters(in: .whitespacesAndNewlines)
      
      // Part 1
      var houses: [Coord: Int] = [Coord(x: 0, y: 0): 1]
      var x = 0
      var y = 0
      
      for direction in directions {
        switch direction {
        case "^":
          y += 1
        case ">":
          x += 1
        case "<":
          x -= 1
        case "v":
          y -= 1
        default:
          break
        }
        
        let coord = Coord(x: x, y: y)
        houses[coord, default: 0] += 1
      }
      
      print("Day 3 Part 1: \(houses.count)")
      
      // Part 2
      var housesP2: [Coord: Int] = [Coord(x: 0, y: 0): 1]
      var dalek: [Coord: Int] = [:]
      var santaX = 0
      var santaY = 0
      var dalekX = 0
      var dalekY = 0
      var isSanta = true
      
      for direction in directions {
        switch direction {
        case "^":
          if isSanta {
            santaY += 1
          } else {
            dalekY += 1
          }
        case ">":
          if isSanta {
            santaX += 1
          } else {
            dalekX += 1
          }
        case "<":
          if isSanta {
            santaX -= 1
          } else {
            dalekX -= 1
          }
        case "v":
          if isSanta {
            santaY -= 1
          } else {
            dalekY -= 1
          }
        default:
          break
        }
        
        if isSanta {
          let coord = Coord(x: santaX, y: santaY)
          if housesP2[coord] != nil {
            housesP2[coord]! += 1
          } else {
            if dalek[coord] == nil {
              housesP2[coord] = 1
            }
          }
        } else {
          let coord = Coord(x: dalekX, y: dalekY)
          if dalek[coord] != nil {
            dalek[coord]! += 1
          } else {
            if housesP2[coord] == nil {
              dalek[coord] = 1
            }
          }
        }
        
        isSanta.toggle()
      }
      
      let total = housesP2.count + dalek.count
      print("Day 3 Part 2: \(total)")
      
    } catch {
      print("Error reading file: \(error)")
    }
  }
}
