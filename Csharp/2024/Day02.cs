using System;
using System.IO;
using System.Linq;
using System.Net;
using System.Text.RegularExpressions;


namespace Day02
{
    class Program
    {
        static bool Are_levels_safe(List<int> levels)
        {
            // The levels are either all increasing or all decreasing.
            // Any two adjacent levels differ by at least one and at most three.
            bool first_val = true;
            int prev_val = 0;
            bool increasing = false;
            bool decreasing = false;
            bool safe_level = true;
                    
            foreach (var l in levels)
            {
                if (first_val)
                {
                    first_val = false;
                    prev_val = l;
                    continue;
                }

                if (l < prev_val)
                {
                    decreasing = true;
                }
                else if (l > prev_val)
                {
                    increasing = true;
                }

                if ((l == prev_val) || (l < prev_val && increasing) || (l > prev_val && decreasing))
                {
                    safe_level = false;
                    break;
                }

                int delta_l = Math.Abs(l - prev_val);
                if (delta_l == 0 || delta_l > 3)
                {
                    safe_level = false;
                    break;
                }
                        
                prev_val = l;
            }
            return safe_level;
        }

        static void Main(string[] args)
        {
            string filePath = "../../data/2024/day02.dat";

            int reports = 0;
            int tolerate_reports = 0;

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    List<int> levels = [];

                    levels = Regex.Matches(line, @"\d+")
                                .Select(m => int.Parse(m.Value))
                                .ToList();

                    if (Are_levels_safe(levels))
                    {
                        reports++;
                        tolerate_reports++;
                    }
                    else
                    {
                        for (int i = 0; i < levels.Count; i++)
                        {
                            List<int> tolerable_levels = levels.ToList();
                            tolerable_levels.RemoveAt(i);
                            if (Are_levels_safe(tolerable_levels))
                            {
                                tolerate_reports++;
                                break;
                            }
                        }
                    }
                }
            }

            Console.WriteLine($"2024 Day 02 Part 1: {reports}");
            Console.WriteLine($"2024 Day 02 Part 2: {tolerate_reports}");
        }
    }
}
