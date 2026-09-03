import module java.base;

public class Day14 {
    private record Deer(String name, int speed, int fly, int rest) {}

    public static void main(String[] args) {
        var input = readInput("../../data/2015/day14.dat");
        if (input.isEmpty()) return;

        var pattern = Pattern.compile("(\\w+) can fly (\\d+) km/s for (\\d+) seconds, but then must rest for (\\d+) seconds\\.");
        var deers = new ArrayList<Deer>();
        for (var line : input.lines().toList()) {
            var m = pattern.matcher(line);
            if (!m.matches()) continue;
            deers.add(new Deer(m.group(1),
                Integer.parseInt(m.group(2)),
                Integer.parseInt(m.group(3)),
                Integer.parseInt(m.group(4))));
        }

        var distances = new int[deers.size()];
        var points = new int[deers.size()];
        var maxDist = 0;

        for (var t = 0; t < 2503; t++) {
            maxDist = 0;
            for (var i = 0; i < deers.size(); i++) {
                var d = deers.get(i);
                if (t % (d.fly() + d.rest()) < d.fly()) {
                    distances[i] += d.speed();
                }
                maxDist = Math.max(maxDist, distances[i]);
            }
            for (var i = 0; i < deers.size(); i++) {
                if (distances[i] == maxDist) points[i]++;
            }
        }

        System.out.println("Part 1: " + Arrays.stream(distances).max().getAsInt());
        System.out.println("Part 2: " + Arrays.stream(points).max().getAsInt());
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
