using System;
using System.IO;
using System.Linq;
using System.Net;
using System.Text.RegularExpressions;


namespace Day02
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2020/day02.dat";

            int valid_pass = 0;
            int xor_valid_pass = 0;

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    List<string> parts = line.Split(" ").ToList();
                    List<string> low_hi = parts[0].Split("-").ToList();
                    int min_num = int.Parse(low_hi[0]);
                    int max_num = int.Parse(low_hi[1]);
                    char letter = parts[1][0];
                    int num_present = parts[2].Count(c => c == letter);

                    if (num_present >= min_num && num_present <= max_num)
                    {
                        valid_pass++;
                    }

                    if (parts[2][min_num-1] == letter ^ parts[2][max_num-1] == letter)
                    {
                        xor_valid_pass++;
                    }
                }
            }

            Console.WriteLine($"2020 Day 02 Part 1: {valid_pass}");
            Console.WriteLine($"2020 Day 02 Part 2: {xor_valid_pass}");
        }
    }
}
