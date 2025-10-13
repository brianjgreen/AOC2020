import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * <p>
 * The {@code Day03} class provides solutions for Advent of Code 2015, Day 3:
 * "Perfectly Spherical Houses in a Vacuum". The puzzle describes Santa (and Robo-Santa)
 * delivering presents according to directional instructions contained in a text file.
 * The main tasks are to determine how many unique houses receive at least one present.
 * </p>
 *
 * <p>
 * The class reads the input data from a file, parses it, and computes:
 * <ul>
 *   <li><strong>Part 1:</strong> The number of unique houses visited by Santa, following all directions sequentially.</li>
 *   <li><strong>Part 2:</strong> The number of unique houses visited when Santa and Robo-Santa take turns moving.</li>
 * </ul>
 * </p>
 *
 * <h2>Usage</h2>
 * <pre>
 *   java Day03
 * </pre>
 */
public class Day03 {
     /**
     * Parses the raw input string and splits it into lines.
     *
     * @param inputData the raw input string from the data file
     * @return a {@code List} of lines from the input data
     */
    public static List<String> parseInput(String inputData) {
        String[] lines = inputData.trim().split("\\R");
        return Arrays.asList(lines);
    }

    /**
     * Main entry point. Reads input data from a file, parses it,
     * and prints the solution for both parts.
     *
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        String input;
        // Read input data
        try {
            input = new String(Files.readAllBytes(Paths.get("../../data/2015/day03.dat")));
            // your code...
        } catch (NoSuchFileException e) {
            System.out.println("Data file missing");
            // Optionally, exit or handle differently
            return;
        } catch (IOException ex) {
            return;
        }

        List<String> data = parseInput(input);

        // Solve part 1
        int result1 = solvePart1(data);
        System.out.println("Part 1: " + result1);

        // Solve part 2
        int result2 = solvePart2(data);
        System.out.println("Part 2: " + result2);
    }

    /**
     * Solves Part 1 of Day 3: counts the number of unique houses visited by Santa.
     * Santa follows the given directions and delivers a present to each house visited.
     *
     * @param data the list containing the instruction string
     * @return the number of unique houses that receive at least one present
     */
    private static int solvePart1(List<String> data) {
        Set<String> houses = new HashSet<>();
        int x = 0;
        int y = 0;
        houses.add(x + "," + y);
        char[] directions = data.get(0).toCharArray();

        for (char direction : directions) {
            switch (direction) {
                case '^' -> y++;
                case 'v' -> y--;
                case '>' -> x++;
                case '<' -> x--;
            }
            houses.add(x + "," + y);
        }
        return houses.size();
    }

    /**
     * Solves Part 2 of Day 3: counts the number of unique houses visited by Santa and Robo-Santa.
     * Santa and Robo-Santa take turns following the directions, starting at the same location,
     * and together deliver presents to houses.
     *
     * @param data the list containing the instruction string
     * @return the number of unique houses that receive at least one present
     */
    private static int solvePart2(List<String> data) {
        Set<String> visited = new HashSet<>();
        int sx = 0, sy = 0;
        int rx = 0, ry = 0;
        visited.add("0,0");
        char[] directions = data.get(0).toCharArray();

        for (int i = 0; i < directions.length; i++) {
            int x, y;
            if (i % 2 == 0) {
                // Santa's move
                switch (directions[i]) {
                    case '^' -> sy++;
                    case 'v' -> sy--;
                    case '>' -> sx++;
                    case '<' -> sx--;
                }
                x = sx; y = sy;
            } else {
                // Robo-Santa's move
                switch (directions[i]) {
                    case '^' -> ry++;
                    case 'v' -> ry--;
                    case '>' -> rx++;
                    case '<' -> rx--;
                }
                x = rx; y = ry;
            }
            visited.add(x + "," + y);
        }
        return visited.size();
    }
}