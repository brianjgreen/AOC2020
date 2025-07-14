package org.adventers.guild;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class aoc01_part1 {
    public static void main( String[] args )
    {
        Path filePath = Paths.get("data", "brian_aoc01.dat");
        String content = "1721 979 366 299 675 1456";

        try
        {
            content = Files.readString(filePath);
            // System.out.println(content);
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }

        try (Scanner scanner = new Scanner(content)) {
            List<Integer> list = new ArrayList<>();
            while (scanner.hasNextInt()) {
                list.add(scanner.nextInt());
            }

            int position = 1;
            for (int x: list) {
                List<Integer> y_list = list.subList(position, list.size());
                for (int y: y_list) {
                    // System.out.println(x + "+" + y + "=" + (x + y));
                    if ((x + y) == 2020) {
                        System.out.println("Found it! " + (x * y));
                        System.exit(0);
                    }
                }
                position++;
            }
        }
    }
}
