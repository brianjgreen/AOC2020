package org.adventers.guild;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

/**
 * This class provides a solution to the Advent of Code 2020 Day 1 Part 2 problem.
 * It reads a list of integers from a file, finds three numbers that sum to 2020, 
 * and returns their product.
 * 
 * @author Brian Green
 */
public class aoc01_part2 {

    private static final int TARGET_SUM = 2020;

    /**
     * Reads a list of integers from a file.
     * 
     * @param filePath The path to the file to read.
     * @return A list of integers read from the file.
     * @throws IOException If an I/O error occurs while reading the file.
     */
    private static List<Integer> readIntegersFromFile(Path filePath) throws IOException {
        return Files.lines(filePath)
                .flatMap(line -> Arrays.stream(line.split("\\s+")))
                .map(Integer::parseInt)
                .toList();
    }

    /**
     * Finds three numbers in the given list that sum to the target sum and returns their product.
     * 
     * @param numbers The list of numbers to search.
     * @return The product of the three numbers that sum to the target sum, or throws an exception if no such numbers are found.
     */
    private static int findProductOfThreeNumbersSummingToTarget(List<Integer> numbers) {
        Set<Integer> numSet = new HashSet<>(numbers);
        for (int i = 0; i < numbers.size(); i++) {
            int x = numbers.get(i);
            for (int j = i + 1; j < numbers.size(); j++) {
                int y = numbers.get(j);
                int z = TARGET_SUM - x - y;
                if (numSet.contains(z) && numbers.indexOf(z) > j) {
                    return x * y * z;
                }
            }
        }
        throw new RuntimeException("No three numbers sum to " + TARGET_SUM);
    }

    /**
     * The main entry point of the program.
     * 
     * @param args Command-line arguments (not used).
     */
    public static void main(String[] args) {
        Path filePath = Paths.get("data", "day01.dat");
        try {
            List<Integer> numbers = readIntegersFromFile(filePath);
            int product = findProductOfThreeNumbersSummingToTarget(numbers);
            System.out.println("Found it! " + product);
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
    }
}