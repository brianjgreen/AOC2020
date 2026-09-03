import module java.base;

public class Day02 {
    private static final Pattern PATTERN = Pattern.compile("(\\d+)-(\\d+) (\\w): (\\w+)");

    public static void main(String[] args) {
        var input = readInput("../../data/2020/day02.dat");
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

    private record PasswordPolicy(int min, int max, char token, String password) {
        static PasswordPolicy parse(String line) {
            var matcher = PATTERN.matcher(line);
            return matcher.matches()
                ? new PasswordPolicy(
                    Integer.parseInt(matcher.group(1)),
                    Integer.parseInt(matcher.group(2)),
                    matcher.group(3).charAt(0),
                    matcher.group(4))
                : null;
        }

        long countToken() {
            return password.chars().filter(c -> c == token).count();
        }

        boolean isValidPart1() {
            var count = countToken();
            return count >= min && count <= max;
        }

        boolean isValidPart2() {
            return (password.charAt(min - 1) == token) ^ (password.charAt(max - 1) == token);
        }
    }

    private static int solvePart1(List<String> data) {
        return (int) data.stream()
            .map(PasswordPolicy::parse)
            .filter(Objects::nonNull)
            .filter(PasswordPolicy::isValidPart1)
            .count();
    }

    private static int solvePart2(List<String> data) {
        return (int) data.stream()
            .map(PasswordPolicy::parse)
            .filter(Objects::nonNull)
            .filter(PasswordPolicy::isValidPart2)
            .count();
    }
}
