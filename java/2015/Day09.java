import module java.base;

public class Day09 {
    private static final HashMap<String, Integer> distances = new HashMap<>();
    private static final ArrayList<String> locations = new ArrayList<>();
    private static int minDistance = Integer.MAX_VALUE;
    private static int maxDistance = 0;

    public static void main(String[] args) {
        var input = readInput("../../data/2015/day09.dat");
        if (input.isEmpty()) return;

        var pattern = Pattern.compile("(.+) to (.+) = (\\d+)");
        for (var line : input.lines().toList()) {
            var m = pattern.matcher(line);
            if (!m.matches()) continue;
            var a = m.group(1);
            var b = m.group(2);
            var d = Integer.parseInt(m.group(3));
            distances.put(a + "->" + b, d);
            distances.put(b + "->" + a, d);
            if (!locations.contains(a)) locations.add(a);
            if (!locations.contains(b)) locations.add(b);
        }

        permute(0);
        System.out.println("Part 1: " + minDistance);
        System.out.println("Part 2: " + maxDistance);
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

    private static void permute(int start) {
        if (start == locations.size()) {
            var total = 0;
            for (var i = 1; i < locations.size(); i++) {
                total += distances.get(locations.get(i - 1) + "->" + locations.get(i));
            }
            minDistance = Math.min(minDistance, total);
            maxDistance = Math.max(maxDistance, total);
            return;
        }
        for (var i = start; i < locations.size(); i++) {
            Collections.swap(locations, start, i);
            permute(start + 1);
            Collections.swap(locations, start, i);
        }
    }
}
