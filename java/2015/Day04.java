import module java.base;

public class Day04 {
    public static void main(String[] args) {
        var input = readInput("../../data/2015/day04.dat");
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
        var base = 0;
        while (true) {
            if (md5Hex(input + base).startsWith("00000")) {
                return base;
            }
            base++;
        }
    }

    private static int solvePart2(String input) {
        var base = 0;
        while (true) {
            if (md5Hex(input + base).startsWith("000000")) {
                return base;
            }
            base++;
        }
    }

    private static String md5Hex(String input) {
        try {
            var md = MessageDigest.getInstance("MD5");
            var digest = md.digest(input.getBytes(StandardCharsets.UTF_8));
            var sb = new StringBuilder(digest.length * 2);
            for (var b : digest) {
                sb.append(String.format("%02x", b & 0xff));
            }
            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("MD5 algorithm not available.", e);
        }
    }
}
