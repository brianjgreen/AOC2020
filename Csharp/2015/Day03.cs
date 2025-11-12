using System;
using System.Collections.Generic;
using System.IO;

namespace Day03
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2015/day03.dat";
            string fileContents = File.ReadAllText(filePath);

            var houses = new Dictionary<(int, int), int>();
            var roboHouses = new Dictionary<(int, int), int>();

            int oneX = 0, oneY = 0;
            int santaX = 0, santaY = 0;
            int roboX = 0, roboY = 0;

            houses[(0, 0)] = 1;
            roboHouses[(0, 0)] = 1;

            bool isSanta = true;
            foreach (char c in fileContents)
            {
                int x = 0, y = 0;

                switch (c)
                {
                    case '>': x++; break;
                    case '<': x--; break;
                    case '^': y++; break;
                    case 'v': y--; break;
                }

                oneX += x;
                oneY += y;
                if (houses.ContainsKey((oneX, oneY)))
                {
                    houses[(oneX, oneY)]++;
                }
                else
                {
                    houses[(oneX, oneY)] = 1;   
                }

                if (isSanta)
                {
                    santaX += x;
                    santaY += y;

                    if (roboHouses.ContainsKey((santaX, santaY)))
                    {
                        roboHouses[(santaX, santaY)]++;
                    }
                    else
                    {
                        roboHouses[(santaX, santaY)] = 1;
                    }
                }
                else
                {
                    roboX += x;
                    roboY += y;

                    if (roboHouses.ContainsKey((roboX, roboY)))
                    {
                        roboHouses[(roboX, roboY)]++;
                    }
                    else
                    {
                        roboHouses[(roboX, roboY)] = 1;
                    }
                }

                isSanta = !isSanta;
            }

            Console.WriteLine($"2015 Day 03 Part 1: {houses.Count}");
            Console.WriteLine($"2015 Day 03 Part 2: {roboHouses.Count}");
        }
    }
}
