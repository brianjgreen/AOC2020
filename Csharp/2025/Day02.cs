using System;

namespace Day02
{
    class Program
    {
        static Int64 Get_num_invalid_ids(string range)
        {
            Int64 sum_invalid_ids = 0;

            Int64 start = Int64.Parse(range.Split('-')[0].Trim());
            Int64 end = Int64.Parse(range.Split('-')[1].Trim());

            for (Int64 i = start; i <= end; i++)
            {
                string num = i.ToString();

                int half = num.Length / 2;
                if (num.Substring(0, half) == num.Substring(half))
                {
                    sum_invalid_ids += i;
                }
            }
            return sum_invalid_ids;
        }

        static void Main(string[] args)
        {
            string filePath = "../../data/2025/day02.dat";

            Int64 num_invalid_ids = 0;

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    string[] ranges = line.Split(',');
                    foreach (string set in ranges)
                    {
                        // Console.WriteLine(set);
                        num_invalid_ids += Get_num_invalid_ids(set);
                    }
                }
            }

            Console.WriteLine($"2025 Day 02 Part 1: {num_invalid_ids}");
            // Console.WriteLine($"2025 Day 02 Part 2: {ticks_when_0}");
        }
    }
}
