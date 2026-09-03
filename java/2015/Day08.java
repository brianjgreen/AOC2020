import module java.base;

public class Day08 {
    public static void main(String[] args) {
        var input = readInput("../../data/2015/day08.dat");
        if (input.isEmpty()) return;

        var totalCode = 0;
        var totalMemory = 0;
        var totalEncoded = 0;

        for (var line : input.lines().toList()) {
            var strSize = line.length();
            totalCode += strSize;

            var mem = strSize - 2;
            var encode = strSize + 4;

            for (var i = 1; i < strSize - 1; i++) {
                if (line.charAt(i) == '\\') {
                    encode += 2;
                    mem--;
                    i++;
                    if (line.charAt(i) == 'x') {
                        mem -= 2;
                        encode--;
                    }
                }
            }

            totalMemory += mem;
            totalEncoded += encode;
        }

        System.out.println("Part 1: " + (totalCode - totalMemory));
        System.out.println("Part 2: " + (totalEncoded - totalCode));
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
