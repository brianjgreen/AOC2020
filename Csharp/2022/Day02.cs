using System;
using System.IO;
using System.Linq;
using System.Net;
using System.Text.RegularExpressions;


namespace Day02
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2022/day02.dat";

            // Elf: A for Rock, B for Paper, and C for Scissors
            // You: X for Rock, Y for Paper, and Z for Scissors
            // The score for a single round is the score for the shape you selected
            // (1 for Rock, 2 for Paper, and 3 for Scissors) 
            // plus the score for the outcome of the round
            // (0 if you lost, 3 if the round was a draw, and 6 if you won).
            int rock = 1;
            int paper = 2;
            int scissors = 3;
            int loss = 0;
            int draw = 3;
            int win = 6;
            var outcome = new Dictionary<string, int>
            {
                ["A X"] = rock + draw,
                ["A Y"] = paper + win,
                ["A Z"] = scissors + loss,
                ["B X"] = rock + loss,
                ["B Y"] = paper + draw,
                ["B Z"] = scissors + win,
                ["C X"] = rock + win,
                ["C Y"] = paper + loss,
                ["C Z"] = scissors + draw
            };

            // X means you need to lose, Y means you need to end the round in a draw,
            // and Z means you need to win
            var outcome2 = new Dictionary<string, int>
            {
                ["A X"] = loss + scissors,
                ["A Y"] = draw + rock,
                ["A Z"] = win + paper,
                ["B X"] = loss + rock,
                ["B Y"] = draw + paper,
                ["B Z"] = win + scissors,
                ["C X"] = loss + paper,
                ["C Y"] = draw + scissors,
                ["C Z"] = win + rock
            };

            int score = 0;
            int score2 = 0;
            
            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    score += outcome[line];
                    score2 += outcome2[line];
                }
            }

            Console.WriteLine($"2022 Day 02 Part 1: {score}");
            Console.WriteLine($"2022 Day 02 Part 2: {score2}");
        }
    }
}
