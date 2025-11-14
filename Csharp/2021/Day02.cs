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
            string filePath = "../../data/2021/day02.dat";

            int depth = 0;
            int distance = 0;
            int aim = 0;
            int aim_depth = 0;

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    List<string> parts = line.Split(" ").ToList();
                    string direction = parts[0];
                    int steps = int.Parse(parts[1]);
                    
                    switch (direction)
                    {
                        case "forward":
                            distance += steps;
                            aim_depth += aim * steps;
                            break;
                        case "up":
                            depth -= steps;
                            aim -= steps;
                            break;
                        case "down":
                            depth += steps;
                            aim += steps;
                            break;
                        default:
                            Console.WriteLine("BAD DIRECTION {direction} {steps}");
                            break;
                    }
                }
            }

            Console.WriteLine($"2021 Day 02 Part 1: {depth * distance}");
            Console.WriteLine($"2021 Day 02 Part 2: {aim_depth * distance}");
        }
    }
}
