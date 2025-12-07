using System;

namespace Day06
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2025/day06.dat";

            Int64 total_sum = 0;
            List<Int64> addition = new List<Int64>();
            List<Int64> multiplication = new List<Int64>();
            bool firstLine = true;

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    Int64[] data = [];
                    string[] stringArray = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);
                    if (line.Contains("*"))
                    {
                        int i = 0;
                        foreach (string oper in stringArray)
                        {
                            if (oper == "*")
                            {
                                total_sum += multiplication[i];
                            }
                            else
                            {
                                total_sum += addition[i];
                            }
                            i++;
                        }
                    }
                    else
                    {
                        data = stringArray.Select(Int64.Parse).ToArray();
                    }
                    if (firstLine)
                    {
                        firstLine = false;
                        foreach (Int64 num in data)
                        {
                            addition.Add(num);
                            multiplication.Add(num);
                        }
                    }
                    else
                    {
                        int i = 0;
                        foreach (Int64 num in data)
                        {
                            addition[i] += num;
                            multiplication[i] *= num;
                            i++;
                        }
                    }
                }
            }

            Console.WriteLine($"2025 Day 06 Part 1: {total_sum}");
            // Console.WriteLine($"2025 Day 06 Part 2: {ticks_when_0}");
        }
    }
}
