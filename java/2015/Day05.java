import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day05 {
     /**
     * Parses the raw input string and splits it into lines.
     *
     * @param inputData the raw input string from the data file
     * @return a {@code List} of lines from the input data
     */
    public static List<String> parseInput(String inputData) {
        return Arrays.asList(inputData.strip().split("\\R"));
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
            input = new String(Files.readAllBytes(Paths.get("../../data/2015/day05.dat")));
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

    private static int solvePart1(List<String> data) {
        int nice = 0;
        for (String message : data) {
            // at least three vowels
            int vowels = 0;
            for (char c : message.toCharArray()) {
                if ("aeiou".indexOf(c) >= 0) {
                    vowels++;
                }
            }
            if (vowels < 3) {
                continue;
            }

            // at least one letter appears twice in a row
            boolean hasDouble = false;
            for (int i = 1; i < message.length(); i++) {
                if (message.charAt(i) == message.charAt(i - 1)) {
                    hasDouble = true;
                    break;
                }
            }
            if (!hasDouble) {
                continue;
            }

            // does not contain the strings ab, cd, pq, or xy
            if (message.contains("ab") || message.contains("cd") ||
                message.contains("pq") || message.contains("xy")) {
                continue;
            }

            nice++;
        }
        return nice;
    }

    private static int solvePart2(List<String> data) {
        int nice = 0;
        for (String message : data) {
            // Pair of any two letters that appears at least twice without overlapping
            boolean hasPair = false;
            Map<String, Integer> pairIndices = new HashMap<>();
            for (int i = 0; i < message.length() - 1; i++) {
                String pair = message.substring(i, i + 2);
                if (pairIndices.containsKey(pair) && pairIndices.get(pair) < i - 1) {
                    hasPair = true;
                    break;
                } else if (!pairIndices.containsKey(pair)) {
                    pairIndices.put(pair, i);
                }
            }
            if (!hasPair) {
                // Check all pairs for non-overlap in first loop, then check remainder here.
                // Second loop only needed if not found above.
                outer:
                for (int i = 0; i < message.length() - 1; i++) {
                    String pair = message.substring(i, i + 2);
                    for (int j = i + 2; j < message.length() - 1; j++) {
                        if (message.substring(j, j + 2).equals(pair)) {
                            hasPair = true;
                            break outer;
                        }
                    }
                }
                if (!hasPair) continue;
            }

            // At least one letter which repeats with exactly one letter between them
            boolean hasRepeatWithGap = false;
            for (int i = 0; i < message.length() - 2; i++) {
                if (message.charAt(i) == message.charAt(i + 2)) {
                    hasRepeatWithGap = true;
                    break;
                }
            }
            if (!hasRepeatWithGap) {
                continue;
            }

            nice++;
        }
        return nice;
    }
}