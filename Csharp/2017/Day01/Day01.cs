using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;


namespace Day01
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2017/day01.dat";

            int last_digit = -1;
            int captcha = 0;

            using StreamReader reader = new(filePath);

            int c;
            int prev_c = -1;

            List<int> numbers = [];

            while ((c = reader.Read()) != -1)
            {
                c -= '0';
                if (last_digit == -1)
                {
                    last_digit = c;
                }
                if (c == prev_c)
                {
                    captcha += c;
                }
                prev_c = c;
                numbers.Add(c);
            }

            if (prev_c == last_digit)
            {
                captcha += last_digit;
            }

            int captcha_pt2 = 0;
            int data_len = numbers.Count;
            foreach (int n in Enumerable.Range(0, data_len - 1))
            {
                if (numbers[n] == numbers[(n + (data_len / 2)) % data_len])
                {
                    captcha_pt2 += numbers[n];
                }
            }
            
            Console.WriteLine($"2017 Day 01 Part 1: {captcha}");
            Console.WriteLine($"2017 Day 01 Part 2: {captcha_pt2}");
        }
    }
}
