import module java.base;

public class Day20 {
    public static void main(String[] args) {
        var input = readInput("../../data/2015/day20.dat");
        if (input.isEmpty()) return;

        var minPresents = Integer.parseInt(input.trim());
        var house = 0;
        var presents = 0;

        while (presents < minPresents) {
            presents = 0;
            house++;
            for (var i = 1; i <= (int) Math.sqrt(house); i++) {
                if (house % i == 0) {
                    presents += i * 10;
                    if (i != house / i) presents += (house / i) * 10;
                }
            }
        }
        System.out.println("Part 1: " + house);

        house = 0;
        presents = 0;
        while (presents < minPresents) {
            presents = 0;
            house++;
            for (var i = 1; i <= (int) Math.round(Math.sqrt(house)); i++) {
                if (house % i == 0) {
                    if (i * 50 >= house) presents += i * 11;
                    if (i != house / i && (house / i) * 50 >= house)
                        presents += (house / i) * 11;
                }
            }
        }
        System.out.println("Part 2: " + house);
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
