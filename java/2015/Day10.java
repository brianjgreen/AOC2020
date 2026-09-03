import module java.base;

public class Day10 {
    public static void main(String[] args) {
        var input = readInput("../../data/2015/day10.dat");
        if (input.isEmpty()) return;

        var current = input;
        for (var i = 0; i < 40; i++) {
            current = lookAndSay(current);
        }
        System.out.println("Part 1: " + current.length());

        for (var i = 0; i < 10; i++) {
            current = lookAndSay(current);
        }
        System.out.println("Part 2: " + current.length());
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

    private static String lookAndSay(String s) {
        var sb = new StringBuilder();
        var count = 1;
        for (var i = 1; i <= s.length(); i++) {
            if (i < s.length() && s.charAt(i) == s.charAt(i - 1)) {
                count++;
            } else {
                sb.append(count).append(s.charAt(i - 1));
                count = 1;
            }
        }
        return sb.toString();
    }
}
