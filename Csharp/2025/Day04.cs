using System;

namespace Day04
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2025/day04.dat";

            int num_of_rolls = 0;
            List<string> rows = new List<string>();

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    rows.Add(line);
                }
            }

            string[] grid = rows.ToArray();
            int max_x = rows[0].Length;
            int max_y = rows.Count;
            Console.WriteLine($"{max_x} {max_y}");

            for (int x = 0; x < max_x; x++)
            {
                for (int y = 0; y < max_y; y++)
                {
                    int num_of_found_rolls = 0;
                    if (grid[y][x] != '@')
                    {
                        continue;
                    }
                    for (int delta_x = -1; delta_x <= 1; delta_x++)
                    {
                        for (int delta_y = -1; delta_y <= 1; delta_y++)
                        {
                            int check_for_roll_x = x + delta_x;
                            int check_for_roll_y = y + delta_y;

                            if (
                                (check_for_roll_x >= 0)
                                && (check_for_roll_x < max_x)
                                && (check_for_roll_y >= 0)
                                && (check_for_roll_y < max_y)
                                && grid[check_for_roll_y][check_for_roll_x] == '@'
                            )
                            {
                                num_of_found_rolls++;
                            }
                        }
                    }
                    if (num_of_found_rolls < 5)
                    {
                        num_of_rolls++;
                    }
                }
            }

            Console.WriteLine($"2025 Day 04 Part 1: {num_of_rolls}");
            // Console.WriteLine($"2025 Day 04 Part 2: {ticks_when_0}");
        }
    }
}
