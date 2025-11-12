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
            string filePath = "../../data/2021/day01.dat";

            int num_increases = -1;
            int num_sliding_increses = 0;
            int prev_measure = 0;
            List<int> values = [];
            
            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    int reading = int.Parse(line);
                    if (reading > prev_measure)
                    {
                        num_increases++;
                    }
                    prev_measure = reading;
                    values.Add(reading);
                }
            }

            foreach (int i in Enumerable.Range(0, values.Count - 3))
            {
                if ((values[i + 1] + values[i + 2] + values[i + 3]) > (values[i] + values[i + 1] + values[i + 2]))
                {
                    num_sliding_increses++;
                }
            }
            
            Console.WriteLine($"2021 Day 01 Part 1: {num_increases}");
            Console.WriteLine($"2021 Day 01 Part 2: {num_sliding_increses}");
        }
    }
}
