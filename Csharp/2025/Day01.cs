using System;

namespace Day01
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2025/day01.dat";

            int times_at_0 = 0;
            int ticks_when_0 = 0;
            int dial_num = 50;

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    int rotations = int.Parse(line.Substring(1));
                    int direction = 1;
                    if (line[0] == 'L')
                    {
                        direction = -1;
                    }
                    int new_dial = (dial_num + (direction * rotations)) % 100;

                    int tick_of_dial = dial_num;
                    for (int i = 0; i < rotations; i++)
                    {
                        tick_of_dial += direction;
                        if (tick_of_dial < 0)
                        {
                            tick_of_dial += 100;
                        }
                        else if (tick_of_dial > 99)
                        {
                            tick_of_dial -= 100;
                        }

                        if (tick_of_dial == 0)
                        {
                            ticks_when_0++;
                        }
                    }

                    if (new_dial < 0)
                    {
                        new_dial += 100;
                    }

                    dial_num = new_dial;
                    if (dial_num == 0)
                    {
                        times_at_0++;
                    }
                }
            }

            Console.WriteLine($"2025 Day 01 Part 1: {times_at_0}");
            Console.WriteLine($"2025 Day 01 Part 2: {ticks_when_0}");
        }
    }
}
