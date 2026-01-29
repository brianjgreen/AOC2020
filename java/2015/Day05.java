import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;

public class Day05 {
    public static void main(String[] args) {
        var input = readInput("../../data/2015/day05.dat");
        if (input.isEmpty()) {
            return;
        }

        var data = input.lines().toList();

        // Solve part 1
        var result1 = solvePart1(data);
        System.out.println("Part 1: " + result1);

        // Solve part 2
        var result2 = solvePart2(data);
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

    private static int solvePart1(List<String> data) {
        var nice = 0;
        for (var message : data) {
            if (isNiceStringPart1(message)) {
                nice++;
            }
        }
        return nice;
    }

    private static boolean isNiceStringPart1(String message) {
        // at least three vowels
        var vowels = message.chars().filter(c -> "aeiou".indexOf(c) >= 0).count();
        if (vowels < 3) {
            return false;
        }

        // at least one letter appears twice in a row
        var hasDouble = false;
        for (var i = 1; i < message.length(); i++) {
            if (message.charAt(i) == message.charAt(i - 1)) {
                hasDouble = true;
                break;
            }
        }
        if (!hasDouble) {
            return false;
        }

        // does not contain the strings ab, cd, pq, or xy
        if (message.contains("ab") || message.contains("cd") ||
            message.contains("pq") || message.contains("xy")) {
            return false;
        }

        return true;
    }

    private static int solvePart2(List<String> data) {
        var nice = 0;
        for (var message : data) {
            if (isNiceStringPart2(message)) {
                nice++;
            }
        }
        return nice;
    }

    private static boolean isNiceStringPart2(String message) {
        // Pair of any two letters that appears at least twice without overlapping
        var hasPair = false;
        var pairIndices = new HashMap<String, Integer>();
        for (var i = 0; i < message.length() - 1; i++) {
            var pair = message.substring(i, i + 2);
            if (pairIndices.containsKey(pair) && pairIndices.get(pair) < i - 1) {
                hasPair = true;
                break;
            } else if (!pairIndices.containsKey(pair)) {
                pairIndices.put(pair, i);
            }
        }
        if (!hasPair) {
            for (var i = 0; i < message.length() - 1; i++) {
                var pair = message.substring(i, i + 2);
                for (var j = i + 2; j < message.length() - 1; j++) {
                    if (message.substring(j, j + 2).equals(pair)) {
                        hasPair = true;
                        break;
                    }
                }
                if (hasPair) break;
            }
            if (!hasPair) return false;
        }

        // At least one letter which repeats with exactly one letter between them
        for (var i = 0; i < message.length() - 2; i++) {
            if (message.charAt(i) == message.charAt(i + 2)) {
                return true;
            }
        }
        return false;
    }
}
