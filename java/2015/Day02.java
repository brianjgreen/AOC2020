import module java.base;

public class Day02 {
    private static final Pattern PATTERN = Pattern.compile("(\\d+)x(\\d+)x(\\d+)");

    public static void main(String[] args) {
        var input = readInput("../../data/2015/day02.dat");
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

    private record Dimensions(int length, int width, int height) {
        static Dimensions parse(String line) {
            var matcher = PATTERN.matcher(line);
            return matcher.matches()
                ? new Dimensions(
                    Integer.parseInt(matcher.group(1)),
                    Integer.parseInt(matcher.group(2)),
                    Integer.parseInt(matcher.group(3)))
                : null;
        }

        int surfaceArea() {
            return 2 * (length * width + width * height + height * length);
        }

        int smallestSide() {
            var dims = new int[] { length, width, height };
            Arrays.sort(dims);
            return dims[0] * dims[1];
        }

        int volume() {
            return length * width * height;
        }

        int smallestPerimeter() {
            var dims = new int[] { length, width, height };
            Arrays.sort(dims);
            return 2 * (dims[0] + dims[1]);
        }
    }

    private static int solvePart1(List<String> input) {
        return input.stream()
            .map(Dimensions::parse)
            .filter(Objects::nonNull)
            .mapToInt(d -> d.surfaceArea() + d.smallestSide())
            .sum();
    }

    private static int solvePart2(List<String> input) {
        return input.stream()
            .map(Dimensions::parse)
            .filter(Objects::nonNull)
            .mapToInt(d -> d.smallestPerimeter() + d.volume())
            .sum();
    }
}
