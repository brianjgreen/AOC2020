import module java.base;

public class Day15 {
    private record Ingredient(String name, int capacity, int durability, int flavor, int texture, int calories) {}

    public static void main(String[] args) {
        var input = readInput("../../data/2015/day15.dat");
        if (input.isEmpty()) return;

        var pattern = Pattern.compile("(\\w+): capacity (-?\\d+), durability (-?\\d+), flavor (-?\\d+), texture (-?\\d+), calories (-?\\d+)");
        var ingredients = new ArrayList<Ingredient>();
        for (var line : input.lines().toList()) {
            var m = pattern.matcher(line);
            if (!m.matches()) continue;
            ingredients.add(new Ingredient(m.group(1),
                Integer.parseInt(m.group(2)), Integer.parseInt(m.group(3)),
                Integer.parseInt(m.group(4)), Integer.parseInt(m.group(5)),
                Integer.parseInt(m.group(6))));
        }

        var maxScore = 0;
        var max500CalScore = 0;
        var n = ingredients.size();
        var counts = new int[n];

        while (true) {
            var total = 0;
            for (var c : counts) total += c;
            if (total == 100) {
                var cap = 0; var dur = 0; var fla = 0; var tex = 0; var cal = 0;
                for (var i = 0; i < n; i++) {
                    var ing = ingredients.get(i);
                    cap += counts[i] * ing.capacity();
                    dur += counts[i] * ing.durability();
                    fla += counts[i] * ing.flavor();
                    tex += counts[i] * ing.texture();
                    cal += counts[i] * ing.calories();
                }
                if (cap > 0 && dur > 0 && fla > 0 && tex > 0) {
                    var score = cap * dur * fla * tex;
                    maxScore = Math.max(maxScore, score);
                    if (cal == 500) max500CalScore = Math.max(max500CalScore, score);
                }
            }

            var rollOver = true;
            for (var i = 0; i < n; i++) {
                if (counts[i] < 100) {
                    counts[i]++;
                    rollOver = false;
                    break;
                }
                counts[i] = 0;
            }
            if (rollOver) break;
        }

        System.out.println("Part 1: " + maxScore);
        System.out.println("Part 2: " + max500CalScore);
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
