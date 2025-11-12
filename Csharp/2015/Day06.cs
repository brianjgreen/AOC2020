using System;

namespace Day06
{
    public class Program
    {
        private const int MAX_X = 1000;
        private const int MAX_Y = 1000;

        public static void Main(string[] args)
        {
            string fileContents = System.IO.File.ReadAllText("../../data/2015/day06.dat");
            string[] lines = fileContents.Split('\n');

            bool[,] lights = new bool[MAX_X, MAX_Y];
            int[,] lightsBright = new int[MAX_X, MAX_Y];

            foreach (string line in lines)
            {
                string[] parts = line.Split(' ');
                int startX, startY, endX, endY;
                string action;

                if (parts[0] == "turn")
                {
                    action = parts[1];
                    startX = int.Parse(parts[2].Split(',')[0]);
                    startY = int.Parse(parts[2].Split(',')[1]);
                    endX = int.Parse(parts[4].Split(',')[0]);
                    endY = int.Parse(parts[4].Split(',')[1]);
                }
                else
                {
                    action = parts[0];
                    startX = int.Parse(parts[1].Split(',')[0]);
                    startY = int.Parse(parts[1].Split(',')[1]);
                    endX = int.Parse(parts[3].Split(',')[0]);
                    endY = int.Parse(parts[3].Split(',')[1]);
                }

                ProcessAction(lights, lightsBright, action, startX, startY, endX, endY);
            }

            int lightsOn = CountLightsOn(lights);
            int totalBrightness = CalculateTotalBrightness(lightsBright);

            Console.WriteLine("2015 Day 06 Part 1: " + lightsOn);
            Console.WriteLine("2015 Day 06 Part 2: " + totalBrightness);
        }

        private static void ProcessAction(bool[,] lights, int[,] lightsBright, string action, int startX, int startY, int endX, int endY)
        {
            for (int x = startX; x <= endX; x++)
            {
                for (int y = startY; y <= endY; y++)
                {
                    if (action == "on")
                    {
                        lights[x, y] = true;
                        lightsBright[x, y]++;
                    }
                    else if (action == "off")
                    {
                        lights[x, y] = false;
                        if (lightsBright[x, y] > 0)
                        {
                            lightsBright[x, y]--;
                        }
                    }
                    else if (action == "toggle")
                    {
                        lights[x, y] = !lights[x, y];
                        lightsBright[x, y] += 2;
                    }
                }
            }
        }

        private static int CountLightsOn(bool[,] lights)
        {
            int count = 0;
            for (int x = 0; x < MAX_X; x++)
            {
                for (int y = 0; y < MAX_Y; y++)
                {
                    if (lights[x, y])
                    {
                        count++;
                    }
                }
            }
            return count;
        }

        private static int CalculateTotalBrightness(int[,] lightsBright)
        {
            int total = 0;
            for (int x = 0; x < MAX_X; x++)
            {
                for (int y = 0; y < MAX_Y; y++)
                {
                    total += lightsBright[x, y];
                }
            }
            return total;
        }
    }
}
