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
            string filePath = "../../data/2023/day01.dat";

            int calibration_sum = 0;
            int expanded_calibration_sum = 0;
            var replacements = new Dictionary<string, string>
            {
                {"one", "1"},
                {"two", "2"},
                {"three", "3"},
                {"four", "4"},
                {"five", "5"},
                {"six", "6"},
                {"seven", "7"},
                {"eight", "8"},
                {"nine", "9"},
            };

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    var firstDigit = line.FirstOrDefault(char.IsDigit);
                    var lastDigit = line.LastOrDefault(char.IsDigit);

                    calibration_sum += ((firstDigit - '0') * 10) + (lastDigit - '0');

                    foreach (var replacement in replacements)
                    {
                        line = line.Replace(replacement.Key, replacement.Key + replacement.Key.LastOrDefault());
                    }
                    foreach (var replacement in replacements)
                    {
                        line = line.Replace(replacement.Key, replacement.Value);
                    }
                    firstDigit = line.FirstOrDefault(char.IsDigit);
                    lastDigit = line.LastOrDefault(char.IsDigit);

                    expanded_calibration_sum += ((firstDigit - '0') * 10) + (lastDigit - '0');

                }
            }

            Console.WriteLine($"2023 Day 01 Part 1: {calibration_sum}");
            Console.WriteLine($"2023 Day 01 Part 2: {expanded_calibration_sum}");
        }
    }
}
