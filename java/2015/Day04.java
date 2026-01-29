import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Day04 {
    public static void main(String[] args) {
        var input = readInput("../../data/2015/day04.dat");
        if (input.isEmpty()) {
            return;
        }

        // Solve part 1
        var result1 = solvePart1(input);
        System.out.println("Part 1: " + result1);

        // Solve part 2
        var result2 = solvePart2(input);
        System.out.println("Part 2: " + result2);
    }

    private static String readInput(String filePath) {
        try {
            return Files.readString(Paths.get(filePath)).trim();
        } catch (NoSuchFileException e) {
            System.out.println("Data file missing: " + filePath);
        } catch (IOException ex) {
            // Consider logging the exception
        }
        return "";
    }

    private static int solvePart1(String input) {
        var base = 0;
        while (true) {
            var s = input + base;
            var hash = md5Hex(s);
            if (hash.startsWith("00000")) {
                return base;
            }
            base++;
        }
    }

    private static int solvePart2(String input) {
        var base = 0;
        while (true) {
            var s = input + base;
            var hash = md5Hex(s);
            if (hash.startsWith("000000")) {
                return base;
            }
            base++;
        }
    }

    /**
     * Computes the MD5 hash of the input string and returns it in hexadecimal.
     *
     * @param input String input.
     * @return Lowercase hex representation of MD5 hash.
     */
    public static String md5Hex(String input) {
        try {
            var md = MessageDigest.getInstance("MD5");
            var digest = md.digest(input.getBytes());
            // Convert byte array to hex String
            var sb = new StringBuilder();
            for (var b : digest) {
                sb.append(String.format("%02x", b & 0xff));
            }
            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("MD5 algorithm not available.", e);
        }
    }
}
