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
            string filePath = "../../data/2020/day01.dat";

            int sum_2020_prod = 0;
            bool found_2020 = false;
            bool found_mass_overload = false;
            int mass_overload = 0;
            List<int> values = [];
            
            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    int reading = int.Parse(line);
                    int complement = 2020 - reading;
                    if (!found_2020)
                    {
                        if (values.Contains(complement))
                        {
                            sum_2020_prod = reading * complement;
                            found_2020 = true;
                        }
                    }

                    values.Add(reading);

                }
                
                foreach (int i in Enumerable.Range(0, values.Count - 1))
                {
                    if (!found_mass_overload)
                    {
                        int x = values[i];
                        foreach (int j in Enumerable.Range(i + 1, values.Count - (i + 1)))
                        {
                            int y = values[j];
                            int z = 2020 - x - y;
                            if (values.Contains(z) && (values.IndexOf(z) > j))
                            {
                                found_mass_overload = true;
                                mass_overload = x * y * z;
                                break;
                            }
                        }
                    }
                }
            }

            Console.WriteLine($"2020 Day 01 Part 1: {sum_2020_prod}");
            Console.WriteLine($"2020 Day 01 Part 2: {mass_overload}");
        }
    }
}
