import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;

public class Day01 {
    public static void main(String[] args) {
        String input;
        // Read input data
        try {
            input = Files.readString(Paths.get("../../data/2015/day01.dat"));
            // your code...
        } catch (NoSuchFileException e) {
            System.out.println("Data file missing: input/day01.txt");
            // Optionally, exit or handle differently
            return;
        } catch (IOException ex) {
            return;
        }

        // Solve part 1
        int result1 = solvePart1(input);
        System.out.println("Part 1: " + result1);

        // Solve part 2
        int result2 = solvePart2(input);
        System.out.println("Part 2: " + result2);
    }

    private static int solvePart1(String input) {
        int floor = 0;
        String[] data = input.trim().split("\n");
        for (char move : data[0].toCharArray()) {
            if (move == ')') {
                floor -= 1;
            } else {
                floor += 1;
            }
        }

        return floor;
    }

    private static int solvePart2(String input) {
        int floor = 0;
        int position = 0;
        String[] data = input.trim().split("\n");
        for (char move : data[0].toCharArray()) {
            position += 1;
            if (move == ')') {
                floor -= 1;
            } else {
                floor += 1;
            }
            if (floor == -1) {
                return position;
            }
        }

        return floor;
    }
}