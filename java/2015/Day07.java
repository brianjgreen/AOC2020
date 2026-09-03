import module java.base;

public class Day07 {
    private enum Op { MOV, NOT, AND, OR, LSHIFT, RSHIFT }

    private record Wire(String inputA, String inputB, Op op) {}

    private static final HashMap<String, Wire> wires = new HashMap<>();
    private static final HashMap<String, Integer> cache = new HashMap<>();

    public static void main(String[] args) {
        var input = readInput("../../data/2015/day07.dat");
        if (input.isEmpty()) return;

        for (var line : input.lines().toList()) {
            parseInstruction(line);
        }

        var part1 = evaluate("a");
        System.out.println("Part 1: " + part1);

        wires.put("b", new Wire(String.valueOf(part1), String.valueOf(part1), Op.MOV));
        cache.clear();
        System.out.println("Part 2: " + evaluate("a"));
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

    private static int evaluate(String name) {
        if (cache.containsKey(name)) return cache.get(name);
        var wire = wires.get(name);
        if (wire == null) {
            try { return Integer.parseInt(name); } catch (NumberFormatException e) { return 0; }
        }
        var a = resolve(wire.inputA());
        var b = resolve(wire.inputB());
        var value = switch (wire.op()) {
            case MOV -> a;
            case NOT -> ~a;
            case AND -> a & b;
            case OR -> a | b;
            case LSHIFT -> a << b;
            case RSHIFT -> a >> b;
        };
        value &= 0xFFFF;
        cache.put(name, value);
        return value;
    }

    private static int resolve(String s) {
        try { return Integer.parseInt(s); } catch (NumberFormatException e) { return evaluate(s); }
    }

    private static void parseInstruction(String line) {
        var tokens = line.split(" -> ");
        var target = tokens[1];
        var parts = tokens[0].split(" ");

        if (parts.length == 1) {
            wires.put(target, new Wire(parts[0], parts[0], Op.MOV));
        } else if (parts[0].equals("NOT")) {
            wires.put(target, new Wire(parts[1], parts[1], Op.NOT));
        } else if (parts.length == 3) {
            var op = switch (parts[1]) {
                case "AND" -> Op.AND;
                case "OR" -> Op.OR;
                case "LSHIFT" -> Op.LSHIFT;
                case "RSHIFT" -> Op.RSHIFT;
                default -> Op.MOV;
            };
            wires.put(target, new Wire(parts[0], parts[2], op));
        }
    }
}
