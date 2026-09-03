import module java.base;

public class Day06 {
    private static final int SIZE = 1000;

    public static void main(String[] args) {
        var input = readInput("../../data/2015/day06.dat");
        if (input.isEmpty()) {
            return;
        }

        var lights = new boolean[SIZE][SIZE];
        var brightness = new int[SIZE][SIZE];

        for (var line : input.lines().toList()) {
            var pattern = Pattern.compile("(turn on|turn off|toggle) (\\d+),(\\d+) through (\\d+),(\\d+)");
            var m = pattern.matcher(line);
            if (!m.matches()) continue;

            var action = m.group(1);
            var x1 = Integer.parseInt(m.group(2));
            var y1 = Integer.parseInt(m.group(3));
            var x2 = Integer.parseInt(m.group(4));
            var y2 = Integer.parseInt(m.group(5));

            for (var x = x1; x <= x2; x++) {
                for (var y = y1; y <= y2; y++) {
                    switch (action) {
                        case "turn on" -> { lights[x][y] = true; brightness[x][y]++; }
                        case "turn off" -> { lights[x][y] = false; if (brightness[x][y] > 0) brightness[x][y]--; }
                        case "toggle" -> { lights[x][y] = !lights[x][y]; brightness[x][y] += 2; }
                    }
                }
            }
        }

        var lightsOn = 0;
        var totalBrightness = 0;
        for (var x = 0; x < SIZE; x++) {
            for (var y = 0; y < SIZE; y++) {
                if (lights[x][y]) lightsOn++;
                totalBrightness += brightness[x][y];
            }
        }

        System.out.println("Part 1: " + lightsOn);
        System.out.println("Part 2: " + totalBrightness);
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
