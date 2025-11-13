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
            string filePath = "../../data/2017/day02.dat";

            int checksum = 0;
            int sum_of_results = 0;

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    List<int> numbers = Regex.Matches(line, @"\d+")
                                            .Select(m => int.Parse(m.Value))
                                            .ToList();

                    var sorted_vals = numbers.OrderBy(n => n).ToArray();
                    checksum += Math.Abs(sorted_vals.First() - sorted_vals.Last());

                    for (int i = 0; i < numbers.Count; i++)
                    {
                        for (int j = i + 1; j < numbers.Count; j++)
                        {
                            if (numbers[i] % numbers[j] == 0)
                            {
                                sum_of_results += numbers[i] / numbers[j];
                            }
                            else if (numbers[j] % numbers[i] == 0)
                            {
                                sum_of_results += numbers[j] / numbers[i];
                            }
                        }
                    }
                }
            }

            Console.WriteLine($"2017 Day 02 Part 1: {checksum}");
            Console.WriteLine($"2017 Day 02 Part 2: {sum_of_results}");
        }
    }
}
