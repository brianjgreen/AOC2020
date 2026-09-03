import module java.base;

public class Day17 {
    private static final int TARGET = 150;

    public static void main(String[] args) {
        var input = readInput("../../data/2015/day17.dat");
        if (input.isEmpty()) return;

        var containers = input.lines()
            .map(Integer::parseInt)
            .toList();

        var numCombos = 0;
        var minContainers = containers.size();
        var minContainerCount = 0;

        for (var mask = 0; mask < (1 << containers.size()); mask++) {
            var volume = 0;
            var count = Integer.bitCount(mask);
            for (var i = 0; i < containers.size(); i++) {
                if ((mask & (1 << i)) != 0) {
                    volume += containers.get(i);
                }
            }
            if (volume == TARGET) {
                numCombos++;
                if (count < minContainers) {
                    minContainers = count;
                    minContainerCount = 1;
                } else if (count == minContainers) {
                    minContainerCount++;
                }
            }
        }

        System.out.println("Part 1: " + numCombos);
        System.out.println("Part 2: " + minContainerCount);
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
