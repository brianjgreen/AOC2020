import module java.base;

public class Day16 {
    private record Sue(int num, Integer children, Integer cats, Integer samoyeds, Integer pomeranians,
                       Integer akitas, Integer vizslas, Integer goldfish, Integer trees, Integer cars, Integer perfumes) {}

    public static void main(String[] args) {
        var input = readInput("../../data/2015/day16.dat");
        if (input.isEmpty()) return;

        var pattern = Pattern.compile("Sue (\\d+): (\\w+): (\\d+), (\\w+): (\\d+), (\\w+): (\\d+)");
        var sues = new ArrayList<Sue>();
        for (var line : input.lines().toList()) {
            var m = pattern.matcher(line);
            if (!m.matches()) continue;
            var num = Integer.parseInt(m.group(1));
            var props = new HashMap<String, Integer>();
            for (var g = 0; g < 3; g++) {
                props.put(m.group(2 + g * 2), Integer.parseInt(m.group(3 + g * 2)));
            }
            sues.add(new Sue(num,
                props.getOrDefault("children", null),
                props.getOrDefault("cats", null),
                props.getOrDefault("samoyeds", null),
                props.getOrDefault("pomeranians", null),
                props.getOrDefault("akitas", null),
                props.getOrDefault("vizslas", null),
                props.getOrDefault("goldfish", null),
                props.getOrDefault("trees", null),
                props.getOrDefault("cars", null),
                props.getOrDefault("perfumes", null)));
        }

        // Part 1: exact match
        for (var sue : sues) {
            if (matchesPart1(sue)) {
                System.out.println("Part 1: " + sue.num());
                break;
            }
        }

        // Part 2: range match
        for (var sue : sues) {
            if (matchesPart2(sue)) {
                System.out.println("Part 2: " + sue.num());
                break;
            }
        }
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

    private static boolean matchesPart1(Sue sue) {
        return matches(sue.children(), 3) && matches(sue.cats(), 7) &&
               matches(sue.samoyeds(), 2) && matches(sue.pomeranians(), 3) &&
               matches(sue.akitas(), 0) && matches(sue.vizslas(), 0) &&
               matches(sue.goldfish(), 5) && matches(sue.trees(), 3) &&
               matches(sue.cars(), 2) && matches(sue.perfumes(), 1);
    }

    private static boolean matches(Integer sueVal, int target) {
        return sueVal == null || sueVal == target;
    }

    private static boolean matchesPart2(Sue sue) {
        return matches(sue.children(), 3) && gt(sue.cats(), 7) &&
               matches(sue.samoyeds(), 2) && lt(sue.pomeranians(), 3) &&
               matches(sue.akitas(), 0) && matches(sue.vizslas(), 0) &&
               lt(sue.goldfish(), 5) && gt(sue.trees(), 3) &&
               matches(sue.cars(), 2) && matches(sue.perfumes(), 1);
    }

    private static boolean gt(Integer sueVal, int target) {
        return sueVal == null || sueVal > target;
    }

    private static boolean lt(Integer sueVal, int target) {
        return sueVal == null || sueVal < target;
    }
}
