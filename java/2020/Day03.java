import module java.base;

public class Day03 {
    private record Slope(int x, int y) {}

    private static final List<Slope> SLOPES = List.of(
        new Slope(3, 1),
        new Slope(1, 1),
        new Slope(5, 1),
        new Slope(7, 1),
        new Slope(1, 2)
    );

    public static void main(String[] args) {
        var input = readInput("../../data/2020/day03.dat");
        if (input.isEmpty()) {
            return;
        }

        var data = input.lines().toList();
        var xMax = data.getFirst().length();

        var result = SLOPES.stream()
            .mapToLong(slope -> countTrees(data, xMax, slope.x(), slope.y()))
            .reduce(1L, (a, b) -> a * b);
        System.out.println("Part 1: " + countTrees(data, xMax, 3, 1));
        System.out.println("Part 2: " + result);
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

    private static long countTrees(List<String> data, int xMax, int xOffset, int yOffset) {
        var x = 0;
        var totalTrees = 0L;
        for (var y = 0; y < data.size(); y += yOffset) {
            totalTrees += data.get(y).charAt(x) == '#' ? 1 : 0;
            x = (x + xOffset) % xMax;
        }
        return totalTrees;
    }
}
