package org.adventers.guild;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

/**
 * The Day03 class provides a solution to the Advent of Code Day 3 problem.
 * It reads a grid of characters from a file, counts the number of trees encountered
 * when traversing the grid with different slopes, and prints the results.
 */
public class Day03 {
    /**
     * An array of slopes to traverse the grid with. Each slope is represented as an array of two integers,
     * where the first element is the x-offset and the second element is the y-offset.
     */
    private static final int[][] SLOPES = {{3, 1}, {1, 1}, {5, 1}, {7, 1}, {1, 2}};

    /**
     * The main entry point of the program. Reads the grid data from a file, counts the trees for each slope,
     * and prints the results.
     * 
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        try {
            String[] data = Files.readAllLines(Paths.get("data", "day03.dat")).toArray(new String[0]);
            int xMax = data[0].length();
            long result = 1;
            for (int[] slope : SLOPES) {
                long trees = countTrees(data, xMax, slope[0], slope[1]);
                if (slope[0] == 3 && slope[1] == 1) {
                    System.out.println("Total trees: " + trees);
                } else {
                    System.out.println("Slope (" + slope[0] + ", " + slope[1] + "): " + trees + " trees");
                }
                result *= trees;
            }
            System.out.println("Big number: " + result);
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
    }

    /**
     * Counts the number of trees encountered when traversing the grid with the given slope.
     * 
     * @param data    the grid data as an array of strings
     * @param xMax    the maximum x-coordinate of the grid
     * @param xOffset the x-offset of the slope
     * @param yOffset the y-offset of the slope
     * @return the number of trees encountered
     */
    private static long countTrees(String[] data, int xMax, int xOffset, int yOffset) {
        int x = 0;
        long totalTrees = 0;
        for (int y = 0; y < data.length; y += yOffset) {
            totalTrees += data[y].charAt(x) == '#' ? 1 : 0;
            x = (x + xOffset) % xMax;
        }
        return totalTrees;
    }
}