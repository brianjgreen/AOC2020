import module java.base;

public class Day21 {
    private record Item(String name, int cost, int damage, int armor) {}

    private static final Item[] WEAPONS = {
        new Item("Dagger", 8, 4, 0), new Item("Shortsword", 10, 5, 0),
        new Item("Warhammer", 25, 6, 0), new Item("Longsword", 40, 7, 0),
        new Item("Greataxe", 74, 8, 0)
    };
    private static final Item[] ARMOR = {
        new Item("None", 0, 0, 0), new Item("Leather", 13, 0, 1),
        new Item("Chainmail", 31, 0, 2), new Item("Splintmail", 53, 0, 3),
        new Item("Bandedmail", 75, 0, 4), new Item("Platemail", 102, 0, 5)
    };
    private static final Item[] RINGS = {
        new Item("None", 0, 0, 0), new Item("Damage +1", 25, 1, 0),
        new Item("Damage +2", 50, 2, 0), new Item("Damage +3", 100, 3, 0),
        new Item("Defense +1", 20, 0, 1), new Item("Defense +2", 40, 0, 2),
        new Item("Defense +3", 80, 0, 3)
    };

    public static void main(String[] args) {
        var input = readInput("../../data/2015/day21.dat");
        if (input.isEmpty()) return;

        var bossHp = 0; var bossAtt = 0; var bossDef = 0;
        for (var line : input.lines().toList()) {
            var parts = line.split(": ");
            var val = Integer.parseInt(parts[1]);
            switch (parts[0]) {
                case "Hit Points" -> bossHp = val;
                case "Damage" -> bossAtt = val;
                case "Armor" -> bossDef = val;
            }
        }

        var minCost = Integer.MAX_VALUE;
        var maxCost = 0;

        for (var r1 : RINGS) {
            for (var r2 : RINGS) {
                if (r1.cost() == 0 && r2.cost() == 0) continue;
                if (r1.cost() == r2.cost()) continue;
                for (var w : WEAPONS) {
                    for (var a : ARMOR) {
                        var playerDmg = r1.damage() + r2.damage() + w.damage();
                        var playerDef = r1.armor() + r2.armor() + a.armor();
                        var cost = r1.cost() + r2.cost() + w.cost() + a.cost();
                        if (playerWins(bossHp, bossAtt, bossDef, playerDef, playerDmg)) {
                            minCost = Math.min(minCost, cost);
                        } else {
                            maxCost = Math.max(maxCost, cost);
                        }
                    }
                }
            }
        }

        System.out.println("Part 1: " + minCost);
        System.out.println("Part 2: " + maxCost);
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

    private static boolean playerWins(int bossHp, int bossAtt, int bossDef, int playerDef, int playerAtt) {
        var hp = 100;
        while (hp > 0 && bossHp > 0) {
            bossHp -= Math.max(1, playerAtt - bossDef);
            if (bossHp > 0) hp -= Math.max(1, bossAtt - playerDef);
        }
        return hp > 0;
    }
}
