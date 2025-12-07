using System;

namespace Day05
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2025/day05.dat";

            int total_fresh = 0;
            List<(Int64 Min, Int64 Max)> freshRange = new List<(Int64 Min, Int64 Max)>();

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    if (line.Length == 0)
                    {
                        continue;
                    }
                    else if (line.Contains("-"))
                    {
                        string[] stringArray = line.Split(
                            '-',
                            StringSplitOptions.RemoveEmptyEntries
                        );
                        Int64[] data = stringArray.Select(Int64.Parse).ToArray();
                        freshRange.Add((Min: data[0], Max: data[1]));
                    }
                    else
                    {
                        Int64 data = Int64.Parse(line);
                        foreach ((Int64 Min, Int64 Max) fresh in freshRange)
                        {
                            if ((data >= fresh.Min) && (data <= fresh.Max))
                            {
                                total_fresh++;
                                break;
                            }
                        }
                    }
                }
            }

            Console.WriteLine($"2025 Day 06 Part 1: {total_fresh}");
            // Console.WriteLine($"2025 Day 06 Part 2: {ticks_when_0}");
        }
    }
}
