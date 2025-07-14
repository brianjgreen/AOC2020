package org.adventers.guild;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class aoc01_part1 {
    public static void main(String[] args) {
        Path filePath = Paths.get("data", "day01.dat");

        try {
            String content = Files.readString(filePath);
            try (Scanner scanner = new Scanner(content)) {
                Set<Integer> numbers = new HashSet<>();
                while (scanner.hasNextInt()) {
                    int num = scanner.nextInt();
                    int complement = 2020 - num;
                    if (numbers.contains(complement)) {
                        System.out.println("Found it! " + (num * complement));
                        System.exit(0);
                    }
                    numbers.add(num);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}