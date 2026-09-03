import module java.base;

public class Day11 {
    private static final String ALPHA = "abcdefghjkmnpqrstuvwxyz";

    public static void main(String[] args) {
        var input = readInput("../../data/2015/day11.dat");
        if (input.isEmpty()) return;

        var password = new StringBuilder(input.trim());
        findValidPassword(password);
        System.out.println("Part 1: " + password);

        findValidPassword(password);
        System.out.println("Part 2: " + password);
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

    private static void findValidPassword(StringBuilder password) {
        do {
            increment(password);
        } while (!isValid(password));
    }

    private static void increment(StringBuilder password) {
        var pos = password.length() - 1;
        while (pos >= 0) {
            var c = password.charAt(pos);
            var idx = ALPHA.indexOf(c);
            if (idx == ALPHA.length() - 1) {
                password.setCharAt(pos, ALPHA.charAt(0));
                pos--;
            } else {
                password.setCharAt(pos, ALPHA.charAt(idx + 1));
                break;
            }
        }
    }

    private static boolean isValid(StringBuilder password) {
        var s = password.toString();
        return hasStraightOfThree(s) && hasTwoPairs(s);
    }

    private static boolean hasStraightOfThree(String s) {
        for (var i = 0; i <= ALPHA.length() - 3; i++) {
            var triple = "" + ALPHA.charAt(i) + ALPHA.charAt(i + 1) + ALPHA.charAt(i + 2);
            if (s.contains(triple)) return true;
        }
        return false;
    }

    private static boolean hasTwoPairs(String s) {
        var count = 0;
        for (var i = 0; i < ALPHA.length(); i++) {
            var pair = "" + ALPHA.charAt(i) + ALPHA.charAt(i);
            if (s.contains(pair)) {
                count++;
                if (count == 2) return true;
            }
        }
        return false;
    }
}
