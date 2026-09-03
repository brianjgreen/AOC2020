import module java.base;

public class Day18 {
    private static final int SIZE = 100;
    private static final int STEPS = 100;

    public static void main(String[] args) {
        var input = readInput("../../data/2015/day18.dat");
        if (input.isEmpty()) return;

        var init = new boolean[SIZE][SIZE];
        var row = 0;
        for (var line : input.lines().toList()) {
            for (var col = 0; col < SIZE; col++) {
                init[row][col] = line.charAt(col) == '#';
            }
            row++;
        }

        var lights = new boolean[SIZE][SIZE];
        for (var x = 0; x < SIZE; x++)
            System.arraycopy(init[x], 0, lights[x], 0, SIZE);
        cycle(lights, false);
        System.out.println("Part 1: " + countOn(lights));

        for (var x = 0; x < SIZE; x++)
            System.arraycopy(init[x], 0, lights[x], 0, SIZE);
        cycle(lights, true);
        System.out.println("Part 2: " + countOn(lights));
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

    private static void cycle(boolean[][] lights, boolean stuck) {
        if (stuck) setStuckCorners(lights);
        for (var step = 0; step < STEPS; step++) {
            var next = new boolean[SIZE][SIZE];
            for (var x = 0; x < SIZE; x++) {
                for (var y = 0; y < SIZE; y++) {
                    var on = countNeighbors(lights, x, y);
                    next[x][y] = lights[x][y] ? (on == 2 || on == 3) : (on == 3);
                }
            }
            for (var x = 0; x < SIZE; x++)
                System.arraycopy(next[x], 0, lights[x], 0, SIZE);
            if (stuck) setStuckCorners(lights);
        }
    }

    private static void setStuckCorners(boolean[][] lights) {
        lights[0][0] = true;
        lights[0][SIZE - 1] = true;
        lights[SIZE - 1][0] = true;
        lights[SIZE - 1][SIZE - 1] = true;
    }

    private static int countNeighbors(boolean[][] lights, int x, int y) {
        var count = 0;
        for (var dx = -1; dx <= 1; dx++) {
            for (var dy = -1; dy <= 1; dy++) {
                if (dx == 0 && dy == 0) continue;
                var nx = x + dx;
                var ny = y + dy;
                if (nx >= 0 && nx < SIZE && ny >= 0 && ny < SIZE && lights[nx][ny]) {
                    count++;
                }
            }
        }
        return count;
    }

    private static int countOn(boolean[][] lights) {
        var total = 0;
        for (var x = 0; x < SIZE; x++)
            for (var y = 0; y < SIZE; y++)
                if (lights[x][y]) total++;
        return total;
    }
}
