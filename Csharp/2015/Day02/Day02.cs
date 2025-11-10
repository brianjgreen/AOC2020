using System;
using System.IO;
using System.Linq;

namespace Day02
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2015/day02.dat";

            int totalArea = 0;
            int totalRibbon = 0;

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    string[] dimensions = line.Split('x');
                    int[] dims = dimensions.Select(int.Parse).ToArray();
                    Array.Sort(dims);

                    int area = 2 * (dims[0] * dims[1] + dims[1] * dims[2] + dims[0] * dims[2]) + dims[0] * dims[1];
                    int ribbon = 2 * (dims[0] + dims[1]) + dims[0] * dims[1] * dims[2];

                    totalArea += area;
                    totalRibbon += ribbon;
                }
            }

            Console.WriteLine($"2015 Day 02 Part 1: {totalArea}");
            Console.WriteLine($"2015 Day 02 Part 2: {totalRibbon}");
        }
    }
}
