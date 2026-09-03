import module java.base;

public class Day05 {
    public static void main(String[] args) {
        var input = readInput("../../data/2015/day05.dat");
        if (input.isEmpty()) {
            return;
        }

        var data = input.lines().toList();

        System.out.println("Part 1: " + solvePart1(data));
        System.out.println("Part 2: " + solvePart2(data));
    }

    private static String readInput(String filePath) {
        try {
            return Files.readString(Paths.get(filePath)).trim();
        } catch (NoSuchFileException e) {
            System.out.println("Data file missing: " + filePath);
        } catch (IOException ex) {
        }
        return "";
    }

    private static int solvePart1(List<String> data) {
        return (int) data.stream().filter(Day05::isNiceStringPart1).count();
    }

    private static boolean isNiceStringPart1(String message) {
        var vowels = message.chars().filter(c -> "aeiou".indexOf(c) >= 0).count();
        if (vowels < 3) {
            return false;
        }

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

        return !message.contains("ab") && !message.contains("cd") &&
               !message.contains("pq") && !message.contains("xy");
    }

    private static int solvePart2(List<String> data) {
        return (int) data.stream().filter(Day05::isNiceStringPart2).count();
    }

    private static boolean isNiceStringPart2(String message) {
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
            return false;
        }

        for (var i = 0; i < message.length() - 2; i++) {
            if (message.charAt(i) == message.charAt(i + 2)) {
                return true;
            }
        }
        return false;
    }
}
