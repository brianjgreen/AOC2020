import module java.base;

public class Day01 {
    public static void main(String[] args) {
        var input = readInput("../../data/2020/day01.dat");
        if (input.isEmpty()) {
            return;
        }

        var numbers = input.lines()
            .map(Integer::parseInt)
            .toList();

        System.out.println("Part 1: " + solvePart1(numbers));
        System.out.println("Part 2: " + solvePart2(numbers));
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

    private static int solvePart1(List<Integer> numbers) {
        var numSet = new HashSet<>(numbers);
        for (var num : numbers) {
            var complement = 2020 - num;
            if (numSet.contains(complement)) {
                return num * complement;
            }
        }
        throw new RuntimeException("No two numbers sum to 2020");
    }

    private static int solvePart2(List<Integer> numbers) {
        var numSet = new HashSet<>(numbers);
        for (var i = 0; i < numbers.size(); i++) {
            var x = numbers.get(i);
            for (var j = i + 1; j < numbers.size(); j++) {
                var y = numbers.get(j);
                var z = 2020 - x - y;
                if (numSet.contains(z) && numbers.indexOf(z) > j) {
                    return x * y * z;
                }
            }
        }
        throw new RuntimeException("No three numbers sum to 2020");
    }
}
