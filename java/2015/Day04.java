import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;

public class Day04 {
     /**
     * Parses the raw input string and splits it into lines.
     *
     * @param inputData the raw input string from the data file
     * @return a {@code List} of lines from the input data
     */
    public static List<String> parseInput(String inputData) {
        return List.of(inputData.trim().split("\\R"));
    }

    /**
     * Main entry point. Reads input data from a file, parses it,
     * and prints the solution for both parts.
     *
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        String input;
        // Read input data
        try {
            input = new String(Files.readAllBytes(Paths.get("../../data/2015/day04.dat")));
            // your code...
        } catch (NoSuchFileException e) {
            System.out.println("Data file missing");
            // Optionally, exit or handle differently
            return;
        } catch (IOException ex) {
            return;
        }

        List<String> data = parseInput(input);

        // Solve part 1
        int result1 = solvePart1(data);
        System.out.println("Part 1: " + result1);

        // Solve part 2
        int result2 = solvePart2(data);
        System.out.println("Part 2: " + result2);
    }

    /**
     * Computes the MD5 hash of the input string and returns it in hexadecimal.
     *
     * @param input String input.
     * @return Lowercase hex representation of MD5 hash.
     */
    public static String md5Hex(String input) {
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] digest = md.digest(input.getBytes());
            // Convert byte array to hex String
            StringBuilder sb = new StringBuilder();
            for (byte b : digest) {
                sb.append(String.format("%02x", b & 0xff));
            }
            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("MD5 algorithm not available.", e);
        }
    }

    private static int solvePart1(List<String> data) {
        int base = 0;
        String key = data.get(0);
        while (true) {
            String s = key + base;
            String hash = md5Hex(s);
            if (hash.startsWith("00000")) {
                return base;
            }
            base++;
        }
    }

    private static int solvePart2(List<String> data) {
        int base = 0;
        String key = data.get(0);
        while (true) {
            String s = key + base;
            String hash = md5Hex(s);
            if (hash.startsWith("000000")) {
                return base;
            }
            base++;
        }
    }
}