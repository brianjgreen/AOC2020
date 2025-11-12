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
            string filePath = "../../data/2024/day01.dat";

            int total_distamce = 0;
            int similarity = 0;
            List<int> left_vals = [];
            List<int> right_vals = [];

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    string[] substrings = line.Split(["   "], StringSplitOptions.None);

                    left_vals.Add(int.Parse(substrings[0]));
                    right_vals.Add(int.Parse(substrings[1]));
                }
            }

            var sorted_left = left_vals.OrderBy(n => n).ToArray();
            var sorted_right = right_vals.OrderBy(n => n).ToArray();

            foreach (int i in Enumerable.Range(0, left_vals.Count))
            {
                int dist = Math.Abs(sorted_left[i] - sorted_right[i]);
                total_distamce += dist;

                int count = sorted_right.Count(n => n == sorted_left[i]);
                similarity += sorted_left[i] * count;
            }
            Console.WriteLine($"2024 Day 01 Part 1: {total_distamce}");
            Console.WriteLine($"2024 Day 01 Part 2: {similarity}");
        }
    }
}
