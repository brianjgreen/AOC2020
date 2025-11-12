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
            string filePath = "../../data/2019/day01.dat";

            int total_mass = 0;
            int mass = 0;
            int mass_overload = 0;
            
            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    double reading = int.Parse(line);
                    mass = (int)Math.Floor(reading / 3) - 2;
                    total_mass += mass;
                    while (mass > 0)
                    {
                        mass_overload += mass;
                        double mass_again = mass;
                        mass = (int)Math.Floor(mass_again / 3) - 2;
                    }
                }
            }

            Console.WriteLine($"2019 Day 01 Part 1: {total_mass}");
            Console.WriteLine($"2019 Day 01 Part 2: {mass_overload}");
        }
    }
}
