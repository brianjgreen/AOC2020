package org.adventers.guild;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

/**
 * Solves Day 2 of the Advent of Code challenge.
 */
public class Day02 {

    /**
     * Main entry point for the program.
     * 
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        // Define the file path to the input data
        Path filePath = Paths.get("data", "day02.dat");

        try {
            // Read all lines from the input file
            List<String> lines = Files.readAllLines(filePath);

            // Count valid passwords according to the two different policies
            int totalPart1 = countValidPasswordsPart1(lines);
            int totalPart2 = countValidPasswordsPart2(lines);

            // Print the results
            System.out.println("Part 1 Total: " + totalPart1);
            System.out.println("Part 2 Total: " + totalPart2);
        } catch (IOException e) {
            // Handle any errors that occur while reading the file
            System.err.println("Error reading file: " + e.getMessage());
        }
    }

    /**
     * Counts the number of valid passwords according to the first policy.
     * 
     * @param lines List of input lines, each representing a password policy.
     * @return The total number of valid passwords.
     */
    private static int countValidPasswordsPart1(List<String> lines) {
        int total = 0;
        for (String line : lines) {
            // Parse the password policy from the input line
            PasswordPolicy policy = parsePasswordPolicy(line);

            // Check if the password is valid according to the policy
            if (isValidPasswordPart1(policy)) {
                total++;
            }
        }
        return total;
    }

    /**
     * Counts the number of valid passwords according to the second policy.
     * 
     * @param lines List of input lines, each representing a password policy.
     * @return The total number of valid passwords.
     */
    private static int countValidPasswordsPart2(List<String> lines) {
        int total = 0;
        for (String line : lines) {
            // Parse the password policy from the input line
            PasswordPolicy policy = parsePasswordPolicy(line);

            // Check if the password is valid according to the policy
            if (isValidPasswordPart2(policy)) {
                total++;
            }
        }
        return total;
    }

    /**
     * Parses a password policy from a given input line.
     * 
     * @param line Input line representing a password policy.
     * @return The parsed password policy.
     */
    private static PasswordPolicy parsePasswordPolicy(String line) {
        // Split the input line into its components (range, token, password)
        String[] parts = line.split(" ");
        String[] range = parts[0].split("-");
        int min = Integer.parseInt(range[0]);
        int max = Integer.parseInt(range[1]);
        char token = parts[1].charAt(0);
        String password = parts[2];

        // Create a new PasswordPolicy object with the parsed values
        return new PasswordPolicy(min, max, token, password);
    }

    /**
     * Checks if a password is valid according to the first policy.
     * 
     * The password is valid if the count of the token character is within the specified range.
     * 
     * @param policy Password policy to check against.
     * @return True if the password is valid, false otherwise.
     */
    private static boolean isValidPasswordPart1(PasswordPolicy policy) {
        // Count the occurrences of the token character in the password
        int count = countChar(policy.getPassword(), policy.getToken());

        // Check if the count is within the specified range
        return policy.getMin() <= count && count <= policy.getMax();
    }

    /**
     * Checks if a password is valid according to the second policy.
     * 
     * The password is valid if exactly one of the specified indices contains the token character.
     * 
     * @param policy Password policy to check against.
     * @return True if the password is valid, false otherwise.
     */
    private static boolean isValidPasswordPart2(PasswordPolicy policy) {
        String password = policy.getPassword();
        char token = policy.getToken();
        int index1 = policy.getMin() - 1; // Adjust for 0-based indexing
        int index2 = policy.getMax() - 1; // Adjust for 0-based indexing

        // Check if exactly one of the specified indices contains the token character
        return (password.charAt(index1) == token) ^ (password.charAt(index2) == token);
    }

    /**
     * Counts the occurrences of a given character in a string.
     * 
     * @param str String to search in.
     * @param c   Character to count.
     * @return The number of occurrences of the character.
     */
    private static int countChar(String str, char c) {
        int count = 0;
        for (char ch : str.toCharArray()) {
            if (ch == c) {
                count++;
            }
        }
        return count;
    }

    /**
     * Represents a password policy with a minimum and maximum count, a token character, and a password.
     */
    private static class PasswordPolicy {
        private final int min;
        private final int max;
        private final char token;
        private final String password;

        /**
         * Creates a new PasswordPolicy object.
         * 
         * @param min     Minimum count.
         * @param max     Maximum count.
         * @param token   Token character.
         * @param password Password to check.
         */
        public PasswordPolicy(int min, int max, char token, String password) {
            this.min = min;
            this.max = max;
            this.token = token;
            this.password = password;
        }

        /**
         * Gets the minimum count.
         * 
         * @return The minimum count.
         */
        public int getMin() {
            return min;
        }

        /**
         * Gets the maximum count.
         * 
         * @return The maximum count.
         */
        public int getMax() {
            return max;
        }

        /**
         * Gets the token character.
         * 
         * @return The token character.
         */
        public char getToken() {
            return token;
        }

        /**
         * Gets the password.
         * 
         * @return The password.
         */
        public String getPassword() {
            return password;
        }
    }
}