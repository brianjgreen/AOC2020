import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day02 {
    // Parse input: splits text file lines
    public static List<String> parseInput(String inputData) {
        String[] lines = inputData.trim().split("\\R"); // matches all line endings
        return Arrays.asList(lines);
    }

    public static void main(String[] args) {
        String input;
        // Read input data
        try {
            input = new String(Files.readAllBytes(Paths.get("../../data/2015/day02.dat")));
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

    private static int solvePart1(List<String> input) {
        int grandTotal = 0;
        Pattern pattern = Pattern.compile("(\\d+)x(\\d+)x(\\d+)");
        for (String pkg : input) {
            Matcher matcher = pattern.matcher(pkg);
            if (matcher.find()) {
                int length = Integer.parseInt(matcher.group(1));
                int width = Integer.parseInt(matcher.group(2));
                int height = Integer.parseInt(matcher.group(3));
                int[] surfaces = {
                    2 * length * width,
                    2 * width * height,
                    2 * height * length
                };
                int sumSurfaces = surfaces[0] + surfaces[1] + surfaces[2];
                int minSurfaceHalf = Math.min(surfaces[0], Math.min(surfaces[1], surfaces[2])) / 2;
                int total = sumSurfaces + minSurfaceHalf;
                grandTotal += total;
            }
        }
        return grandTotal;
    }

    private static int solvePart2(List<String> input) {
        int grandTotal = 0;
        Pattern pattern = Pattern.compile("(\\d+)x(\\d+)x(\\d+)");
        for (String pkg : input) {
            Matcher matcher = pattern.matcher(pkg);
            if (matcher.find()) {
                int length = Integer.parseInt(matcher.group(1));
                int width  = Integer.parseInt(matcher.group(2));
                int height = Integer.parseInt(matcher.group(3));

                // Compute perimeters of smallest faces
                int[] dims = { length, width, height };
                Arrays.sort(dims);
                int perimeter = 2 * dims[0] + 2 * dims[1];
                int bow = length * width * height;
                int total = perimeter + bow;
                grandTotal += total;
            }
        }
        return grandTotal;
    }
}