import module java.base;

public class Day25 {
    private static final long MULTIPLIER = 252533;
    private static final long MODULUS = 33554393;

    public static void main(String[] args) {
        var input = readInput("../../data/2015/day25.dat");
        if (input.isEmpty()) return;

        var pattern = Pattern.compile(".*row (\\d+), column (\\d+)\\.");
        var m = pattern.matcher(input);
        if (!m.matches()) return;

        var row = Integer.parseInt(m.group(1));
        var col = Integer.parseInt(m.group(2));
        var d = row + col - 1;
        var index = (d - 1) * d / 2 + col;

        var code = 20151125L;
        for (var i = 1; i < index; i++) {
            code = (code * MULTIPLIER) % MODULUS;
        }

        System.out.println("Part 1: " + code);
        System.out.println("Part 2: (requires 49 stars)");
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
}
