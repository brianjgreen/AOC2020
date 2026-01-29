import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Pattern;

public class Day02 {
    public static void main(String[] args) {
        var input = readInput("../../data/2015/day02.dat");
        if (input.isEmpty()) {
            return;
        }

        var data = input.lines().toList();

        // Solve part 1
        var result1 = solvePart1(data);
        System.out.println("Part 1: " + result1);

        // Solve part 2
        var result2 = solvePart2(data);
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

    private static int solvePart1(List<String> input) {
        var grandTotal = 0;
        var pattern = Pattern.compile("(\\d+)x(\\d+)x(\\d+)");
        for (var pkg : input) {
            var matcher = pattern.matcher(pkg);
            if (matcher.matches()) {
                var length = Integer.parseInt(matcher.group(1));
                var width = Integer.parseInt(matcher.group(2));
                var height = Integer.parseInt(matcher.group(3));
                var surfaces = new int[] {
                    length * width,
                    width * height,
                    height * length
                };
                var sumSurfaces = surfaces[0] + surfaces[1] + surfaces[2];
                var minSurface = Arrays.stream(surfaces).min().getAsInt();
                var total = 2 * sumSurfaces + minSurface;
                grandTotal += total;
            }
        }
        return grandTotal;
    }

    private static int solvePart2(List<String> input) {
        var grandTotal = 0;
        var pattern = Pattern.compile("(\\d+)x(\\d+)x(\\d+)");
        for (var pkg : input) {
            var matcher = pattern.matcher(pkg);
            if (matcher.matches()) {
                var length = Integer.parseInt(matcher.group(1));
                var width  = Integer.parseInt(matcher.group(2));
                var height = Integer.parseInt(matcher.group(3));

                // Compute perimeters of smallest faces
                var dims = new int[] { length, width, height };
                Arrays.sort(dims);
                var perimeter = 2 * (dims[0] + dims[1]);
                var bow = length * width * height;
                var total = perimeter + bow;
                grandTotal += total;
            }
        }
        return grandTotal;
    }
}
