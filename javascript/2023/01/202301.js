//
// Avent of Code 2023 Day 1
// Brian Green
//
//

const fs = require("fs");

// Read data from file and return array
async function readLines(filePath) {
  try {
    const fileContent = await fs.promises.readFile(filePath, "utf-8");
    const lines = fileContent.split("\n");
    return lines;
  } catch (err) {
    console.error("Error reading file:", err);
    return [];
  }
}

// Find the first digit in the string
function findFirstDigit(str) {
  for (let i = 0; i < str.length; i++) {
    const char = str.charAt(i);
    if (!isNaN(parseInt(char))) {
      return parseInt(char);
    }
  }
  return null; // Return null if no digit is found
}

// Find the last digit in the string
function findLastDigit(str) {
  for (let i = str.length - 1; i >= 0; i--) {
    const char = str.charAt(i);
    if (!isNaN(parseInt(char))) {
      return parseInt(char);
    }
  }
  return null;
}

// Find the calibration value for part 1 by adding together the first and last digit
function getCalibrationValue(str) {
  readLines(str).then((lines) => {
    let total = 0;
    //console.log(lines);
    lines.forEach((serialnum) => {
      let calibrate = findFirstDigit(serialnum) * 10 + findLastDigit(serialnum);
      //console.log(calibrate)
      total += calibrate;
    });
    console.log(str, "total=", total);
    return total;
  });
}

// Convert the spelled out numbers into digits and then calculate the calibration value
function getCalValPart2(str) {
  let numName = {
    one: "1",
    two: "2",
    three: "3",
    four: "4",
    five: "5",
    six: "6",
    seven: "7",
    eight: "8",
    nine: "9",
  };
  readLines(str).then((lines) => {
    let total = 0;
    //console.log(lines);
    lines.forEach((serialnum) => {
      Object.keys(numName).forEach((key) => {
        // add extra char at the end of each number found so converting the first overlapping
        // number does not corrupt the next number
        // e.g. oneight -> oneeight do this becomes 18 instead of 1ight
        serialnum = serialnum.replaceAll(key, key + key[key.length - 1]);
        //console.log(key, "new=", serialnum);
      });
      Object.keys(numName).forEach((key) => {
        // replace spelled out numbers with its digit
        serialnum = serialnum.replaceAll(key, numName[key]);
        //console.log("newNew=", serialnum);
      });
      total += findFirstDigit(serialnum) * 10 + findLastDigit(serialnum);
      //console.log("total=", total);
    });
    console.log(str, "(part 2) total=", total);
    return total;
  });
}

getCalibrationValue("example.dat");
getCalValPart2("example2.dat");
getCalibrationValue("data.dat");
getCalValPart2("data.dat");
