using System;
using System.IO;
using System.Reflection.Emit;

namespace Day01
{
    public enum Direction
    {
        North,
        East,
        South,
        West
    }

    public struct CompassDirection(int x, int y, Direction left, Direction right)
    {
        public int X = x;
        public int Y = y;
        public Direction Left = left;
        public Direction Right = right;
    }

    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2016/day01.dat";
            string fileContents = File.ReadAllText(filePath);

            string[] directions = fileContents.Split(", ");

            var compass = new Dictionary<Direction, CompassDirection>
            {
                [Direction.North] = new CompassDirection(0, 1, Direction.West, Direction.East),
                [Direction.East] = new CompassDirection(1, 0, Direction.North, Direction.South),
                [Direction.South] = new CompassDirection(0, -1, Direction.East, Direction.West),
                [Direction.West] = new CompassDirection(-1, 0, Direction.South, Direction.North),
            };

            int x = 0, y = 0;
            int dx = 0, dy = 0;
            bool visit_twice = false;
            Direction needle = Direction.North;
            var location = new Dictionary<(int, int), int>();

            foreach (string dir in directions)
            {
                char d = dir[0];
                int steps = int.Parse(dir[1..]);

                if (d == 'L')
                {
                    needle = compass[needle].Left;
                }
                else
                {
                    needle = compass[needle].Right;
                }

                for (int s = 0; s < steps; s++)
                {
                    x += compass[needle].X;
                    y += compass[needle].Y;

                    if (!visit_twice)
                    {
                        if (location.ContainsKey((x, y)))
                        {
                            dx = x;
                            dy = y;
                            visit_twice = true;
                        }
                        else
                        {
                            location[(x, y)] = 1;
                        }
                    }
                }
            }

            int absX = (x < 0) ? -x : x;
            int absY = (y < 0) ? -y : y;
            Console.WriteLine($"2016 Day 01 Part 1: {absX + absY}");
            absX = (dx < 0) ? -dx : dx;
            absY = (dy < 0) ? -dy : dy;
            Console.WriteLine($"2016 Day 01 Part 2: {absX + absY}");
        }
    }
}
