using System;
using System.IO;
using System.Linq;
using System.Net;


namespace Day01
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2022/day01.dat";

            int max_elf_calories = 0;
            List<int> values = [];

            using (StreamReader reader = new(filePath))
            {
                string? line;
                int accum_elf_calories = 0;
                while ((line = reader.ReadLine()) != null)
                {
                    if (string.IsNullOrEmpty(line))
                    {
                        if (accum_elf_calories > max_elf_calories)
                        {
                            max_elf_calories = accum_elf_calories;
                        }
                        accum_elf_calories = 0;
                    }
                    else
                    {
                        accum_elf_calories += int.Parse(line);
                    }
                    values.Add(accum_elf_calories);
                }
            }

            var top_3_elf_calories = values.OrderByDescending(n => n).Take(3);;

            Console.WriteLine($"2022 Day 01 Part 1: {max_elf_calories}");
            Console.WriteLine($"2022 Day 01 Part 2: {top_3_elf_calories.Sum()}");
        }
    }
}
