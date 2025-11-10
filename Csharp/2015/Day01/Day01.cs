using System;
using System.IO;

namespace Day01
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2015/day01.dat";

            int floor = 0;
            int? position = null;
            int i = 0;

            using (StreamReader reader = new(filePath))
            {
                int c;
                while ((c = reader.Read()) != -1)
                {
                    char ch = (char)c;
                    if (ch == ')')
                    {
                        floor--;
                    }
                    else if (ch == '(')
                    {
                        floor++;
                    }

                    i++;

                    if (floor == -1 && position == null)
                    {
                        position = i;
                    }
                }
            }

            Console.WriteLine($"2015 Day 01 Part 1: {floor}");
            Console.WriteLine($"2015 Day 01 Part 2: {position}");
        }
    }
}
