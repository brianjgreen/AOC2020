using System;

namespace Day03
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2025/day03.dat";

            int sum_of_largest = 0;

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    int largest_num = 0;
                    for (int i = 0; i < line.Length; i++)
                    {
                        for (int j = i + 1; j < line.Length; j++)
                        {
                            int num = ((line[i] - '0') * 10) + (line[j] - '0');
                            if (num > largest_num)
                            {
                                largest_num = num;
                            }
                        }
                    }

                    sum_of_largest += largest_num;
                }
            }

            Console.WriteLine($"2025 Day 03 Part 1: {sum_of_largest}");
            // Console.WriteLine($"2025 Day 03 Part 2: {ticks_when_0}");
        }
    }
}
