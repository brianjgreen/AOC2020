using System;
using System.IO;
using System.Linq;
using System.Net;
using System.Text.RegularExpressions;


namespace Day02
{
    class Program
    {
        public static Dictionary<string, int> ParseColorInfo(string inputString)
        {
            // Remove the "Game X:" prefix
            var gameData = inputString.Split(new[] { ": " }, StringSplitOptions.None)[1];
        
            // Initialize a dictionary to store the maximum count for each color
            var colorMaxCount = new Dictionary<string, int>();
        
            // Split the game data into sets
            var sets = gameData.Split(new[] { "; " }, StringSplitOptions.None);
            foreach (var gameSet in sets)
            {
                // Split each set into individual color counts
                var colorCounts = gameSet.Split(new[] { ", " }, StringSplitOptions.None);
                foreach (var colorCount in colorCounts)
                {
                    // Extract count and color
                    var parts = colorCount.Split(' ');
                    var count = int.Parse(parts[0]);
                    var color = parts[1];
                
                    // Update the maximum count for the color
                    if (colorMaxCount.ContainsKey(color))
                    {
                        colorMaxCount[color] = Math.Max(colorMaxCount[color], count);
                    }
                    else
                    {
                        colorMaxCount[color] = count;
                    }
                }
            }
        
            return colorMaxCount;
        }

        static void Main(string[] args)
        {
            string filePath = "../../data/2023/day02.dat";

            int power = 0;
            int game = 1;
            int max_red = 12;
            int max_green = 13;
            int max_blue = 14;
            int possible_games = 0;

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    var result = ParseColorInfo(line);
                    int product = 1;
                    foreach (var bag in result)
                    {
                        product *= bag.Value;
                    }
                    power += product;

                    if (result["red"] <= max_red && result["green"] <= max_green && result["blue"] <= max_blue)
                    {
                        possible_games += game;
                    }
                    game++;
                }
            }

            Console.WriteLine($"2023 Day 02 Part 1: {possible_games}");
            Console.WriteLine($"2023 Day 02 Part 2: {power}");
        }
    }
}
