import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;

public class Day01 {
    public static void main(String[] args) {
        var input = readInput("../../data/2015/day01.dat");
        if (input.isEmpty()) {
            return;
        }

        // Solve part 1
        var result1 = solvePart1(input);
        System.out.println("Part 1: " + result1);

        // Solve part 2
        var result2 = solvePart2(input);
        System.out.println("Part 2: " + result2);
    }

    private static String readInput(String filePath) {
        try {
            return Files.readString(Paths.get(filePath)).trim();
        } catch (NoSuchFileException e) {
            System.out.println("Data file missing: " + filePath);
        } catch (IOException ex) {
            // Consider logging the exception
        }
        return "";
    }

    private static int solvePart1(String input) {
        var floor = 0;
        for (var c : input.toCharArray()) {
            floor += (c == '(') ? 1 : -1;
        }
        return floor;
    }

    private static int solvePart2(String input) {
        var floor = 0;
        var position = 0;
        for (var c : input.toCharArray()) {
            position++;
            floor += (c == '(') ? 1 : -1;
            if (floor == -1) {
                return position;
            }
        }
        return floor;
    }
}
