import module java.base;

public class Day01 {
    public static void main(String[] args) {
        var input = readInput("../../data/2015/day01.dat");
        if (input.isEmpty()) {
            return;
        }

        System.out.println("Part 1: " + solvePart1(input));
        System.out.println("Part 2: " + solvePart2(input));
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

    private static int solvePart1(String input) {
        return input.chars().map(c -> c == '(' ? 1 : -1).sum();
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
