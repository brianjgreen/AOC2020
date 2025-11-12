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
            string filePath = "../../data/2018/day01.dat";

            int freq = 0;
            int result_freq = 0;
            List<int> freq_vals = [];
            List<int> update_vals = [];
            int dup_freq = 0;
            bool found_dup = false;

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    int update = int.Parse(line);
                    freq += update;
                    update_vals.Add(update);
                    freq_vals.Add(freq);
                }

                result_freq = freq;

                while (!found_dup)
                {
                    foreach (int update in update_vals)
                    {
                        freq += update;
                        if (freq_vals.Contains(freq))
                        {
                            found_dup = true;
                            dup_freq = freq;
                            break;
                        }
                        else
                        {
                            freq_vals.Add(freq);
                        }
                    }
                }
            }

            Console.WriteLine($"2018 Day 01 Part 1: {result_freq}");
            Console.WriteLine($"2018 Day 01 Part 2: {dup_freq}");
        }
    }
}
