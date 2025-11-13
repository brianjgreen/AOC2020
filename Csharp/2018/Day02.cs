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
            string filePath = "../../data/2018/day02.dat";

            int num_doubles = 0;
            int num_triples = 0;
            List<string> boxes = [];
            string common_box = "Error";

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    bool found_double = false;
                    bool found_triple = false;

                    foreach (char letter in line)
                    {
                        int count = line.Count(c => c == letter);
                        if (count == 2)
                        {
                            found_double = true;
                        }
                        else if (count == 3)
                        {
                            found_triple = true;
                        }
                    }
                    if (found_double)
                    {
                        num_doubles++;
                    }
                    if (found_triple)
                    {
                        num_triples++;
                    }

                    boxes.Add(line);
                }
            }

            for (int missing_pos = 0; missing_pos < boxes[0].Length; missing_pos++)
            {
                for (int i = 0; i < boxes.Count; i++)
                {
                    for (int j = i + 1; j < boxes.Count; j++)
                    {
                        if (boxes[i].Remove(missing_pos, 1) == boxes[j].Remove(missing_pos, 1))
                        {
                            common_box = boxes[i].Remove(missing_pos, 1);
                        }
                    }
                }
            }

            Console.WriteLine($"2018 Day 02 Part 1: {num_doubles * num_triples}");
            Console.WriteLine($"2018 Day 02 Part 2: {common_box}");
        }
    }
}
