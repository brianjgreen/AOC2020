import module java.base;

public class Day03 {
    public static void main(String[] args) {
        var input = readInput("../../data/2015/day03.dat");
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
        var houses = new HashSet<String>();
        var x = 0;
        var y = 0;
        houses.add("0,0");

        for (var direction : input.toCharArray()) {
            switch (direction) {
                case '^' -> y++;
                case 'v' -> y--;
                case '>' -> x++;
                case '<' -> x--;
            }
            houses.add(x + "," + y);
        }
        return houses.size();
    }

    private static int solvePart2(String input) {
        var visited = new HashSet<String>();
        visited.add("0,0");
        var santa = new int[2];
        var robo = new int[2];

        for (var i = 0; i < input.length(); i++) {
            var pos = i % 2 == 0 ? santa : robo;
            switch (input.charAt(i)) {
                case '^' -> pos[1]++;
                case 'v' -> pos[1]--;
                case '>' -> pos[0]++;
                case '<' -> pos[0]--;
            }
            visited.add(pos[0] + "," + pos[1]);
        }
        return visited.size();
    }
}
