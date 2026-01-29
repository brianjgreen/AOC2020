import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;
import java.util.HashSet;

public class Day03 {
    public static void main(String[] args) {
        var input = readInput("../../data/2015/day03.dat");
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
        var houses = new HashSet<String>();
        var x = 0;
        var y = 0;
        houses.add(x + "," + y);

        for (var direction : input.toCharArray()) {
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

    private static int solvePart2(String input) {
        var visited = new HashSet<String>();
        var sx = 0;
        var sy = 0;
        var rx = 0;
        var ry = 0;
        visited.add("0,0");

        for (var i = 0; i < input.length(); i++) {
            int x, y;
            if (i % 2 == 0) {
                // Santa's move
                switch (input.charAt(i)) {
                    case '^' -> sy++;
                    case 'v' -> sy--;
                    case '>' -> sx++;
                    case '<' -> sx--;
                }
                x = sx;
                y = sy;
            } else {
                // Robo-Santa's move
                switch (input.charAt(i)) {
                    case '^' -> ry++;
                    case 'v' -> ry--;
                    case '>' -> rx++;
                    case '<' -> rx--;
                }
                x = rx;
                y = ry;
            }
            visited.add(x + "," + y);
        }
        return visited.size();
    }
}
