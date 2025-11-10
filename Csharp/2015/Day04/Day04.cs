using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

namespace Day04
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2015/day04.dat";
            string input = File.ReadAllText(filePath).Trim();
            int i = 1;
            bool foundPart1 = false;
            bool foundPart2 = false;

            while (!foundPart1 || !foundPart2)
            {
                string toHash = string.Concat(input, i);
                string md5Hash = CalculateMD5(toHash);

                if (!foundPart1 && md5Hash.StartsWith("00000"))
                {
                    foundPart1 = true;
                    Console.WriteLine($"2015 Day 04 Part 1: {i} {md5Hash}");
                }
                if (!foundPart2 && md5Hash.StartsWith("000000"))
                {
                    foundPart2 = true;
                    Console.WriteLine($"2015 Day 04 Part 2: {i} {md5Hash}");
                }
                i++;
            }
        }

        static string CalculateMD5(string input)
        {
            using var md5 = MD5.Create();
            byte[] inputBytes = Encoding.ASCII.GetBytes(input);
            byte[] hashBytes = md5.ComputeHash(inputBytes);
            return BitConverter.ToString(hashBytes).Replace("-", "").ToLower();
        }
    }
}
