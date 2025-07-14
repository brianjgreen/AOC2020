package org.adventers.guild;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class day02 {
    public static void main( String[] args )
    {
        Path filePath = Paths.get("data", "day02.dat");
        String content = "1-3 a: abcde";

        try
        {
            content = Files.readString(filePath);
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }

        try (Scanner scanner = new Scanner(content)) {
            List<String> list = new ArrayList<>();
            while (scanner.hasNextLine()) {
                list.add(scanner.nextLine());
            }

            int total = 0;
            int total_p2 = 0;

            for (String x: list) {
                // Split on spaces to isolate each part
                String[] parts = x.split(" ");
        
                // Extract first and second numbers from the range
                String[] range = parts[0].split("-");
                int minNumber = Integer.parseInt(range[0]);
                int maxNumber = Integer.parseInt(range[1]);
        
                // Extract the required character (remove the colon)
                char tokenChar = parts[1].charAt(0);
        
                // Extract the substring
                String passwordString = parts[2];

                int count = 0;

                for (int i = 0; i < passwordString.length(); i++) {
                    if (passwordString.charAt(i) == tokenChar) {
                        count++;
                    }
                }
                if ((minNumber <= count) && (count <= maxNumber)) {
                    total++;
                }
                if ((passwordString.charAt(minNumber-1) == tokenChar) ^ (passwordString.charAt(maxNumber-1) == tokenChar)) {
                    total_p2++;
                }
            }

            System.out.println("Part 1 Total: " + total);
            System.out.println("Part 2 Total: " + total_p2);
        }
    }
}
