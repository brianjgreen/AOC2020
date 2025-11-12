using System;

namespace Day05
{
    public class Program
    {
        private static readonly string[] substrings = ["ab", "cd", "pq", "xy"];

        public static void Main(string[] args)
        {
            string fileContents = System.IO.File.ReadAllText("../../data/2015/day05.dat");
            string[] lines = fileContents.Split('\n');

            int good = 0;
            int goodP2 = 0;

            foreach (string line in lines)
            {
                if (IsNice(line))
                {
                    good++;
                }

                if (IsNiceP2(line))
                {
                    goodP2++;
                }
            }

            Console.WriteLine("2015 Day 05 Part 1: " + good);
            Console.WriteLine("2015 Day 05 Part 2: " + goodP2);
        }

        private static bool IsNice(string str)
        {
            int vowelCount = 0;
            bool hasConsecutiveDuplicates = false;

            for (int i = 0; i < str.Length; i++)
            {
                char c = str[i];
                if ("aeiouAEIOU".Contains(c))
                {
                    vowelCount++;
                }
                if (i > 0 && str[i - 1] == c)
                {
                    hasConsecutiveDuplicates = true;
                }
                if (i > 0 && ContainsForbiddenPair(str, i - 1))
                {
                    return false;
                }
            }

            return vowelCount >= 3 && hasConsecutiveDuplicates;
        }

        private static bool ContainsForbiddenPair(string str, int index)
        {
            string pair = str.Substring(index, 2);
            return substrings.Contains(pair);
        }

        private static bool IsNiceP2(string str)
        {
            return PairAppearsTwice(str) && RepeatWithGap(str);
        }

        private static bool ContainsSubstring(string str)
        {
            foreach (string substring in substrings)
            {
                if (str.Contains(substring))
                {
                    return true;
                }
            }
            return false;
        }

        private static int CountVowels(string str)
        {
            int count = 0;
            foreach (char c in str.ToLower())
            {
                if ("aeiou".Contains(c))
                {
                    count++;
                }
            }
            return count;
        }

        private static bool HasConsecutiveDuplicates(string str)
        {
            for (int i = 0; i < str.Length - 1; i++)
            {
                if (str[i] == str[i + 1])
                {
                    return true;
                }
            }
            return false;
        }

        private static bool PairAppearsTwice(string str)
        {
            for (int i = 0; i < str.Length - 1; i++)
            {
                string pair = str.Substring(i, 2);
                if (str.IndexOf(pair, i + 2) != -1)
                {
                    return true;
                }
            }
            return false;
        }

        private static bool RepeatWithGap(string str)
        {
            for (int i = 0; i < str.Length - 2; i++)
            {
                if (str[i] == str[i + 2])
                {
                    return true;
                }
            }
            return false;
        }
    }
}
