using System;
using System.IO;
using System.Linq;
using System.Net;
using System.Security.Cryptography.X509Certificates;


namespace Day02
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2016/day02.dat";

            int[,] keypad = new int[,]
            {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
            };

            char[,] keypad_diamond = new char[,]
            {
                { '0', '0', '1', '0', '0' },
                { '0', '2', '3', '4', '0' } ,
                { '5', '6', '7', '8', '9' },
                { '0', 'A', 'B', 'C', '0' },
                { '0', '0', 'D', '0', '0' }
            };

            int x = 1;
            int y = 1;
            int dx = 0;
            int dy = 2;

            int max_x = 2;
            int max_y = 2;
            int max_dx = 4;
            int max_dy = 4;

            List<int> code = [];
            List<char> code_diamond = [];
            // Console.WriteLine($"0,2 {keypad_diamond[2, 0]}");
            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    foreach (char c in line)
                    {
                        int undo_dx = 0;
                        int undo_dy = 0;

                        switch (c)
                        {
                            case 'U':
                                y--;
                                dy--;
                                undo_dy = 1;
                                break;
                            case 'D':
                                y++;
                                dy++;
                                undo_dy = -1;
                                break;
                            case 'R':
                                x++;
                                dx++;
                                undo_dx = -1;
                                break;
                            case 'L':
                                x--;
                                dx--;
                                undo_dx = 1;
                                break;
                            default:
                                Console.WriteLine($"Invalid instruction {c}");
                                break;
                        }

                        if (x < 0)
                        {
                            x = 0;
                        }
                        if (x > max_x)
                        {
                            x = max_x;
                        }
                        if (y < 0)
                        {
                            y = 0;
                        }
                        if (y > max_y)
                        {
                            y = max_y;
                        }
                        if (dx < 0)
                        {
                            dx = 0;
                        }
                        if (dx > max_dx)
                        {
                            dx = max_dx;
                        }
                        if (dy < 0)
                        {
                            dy = 0;
                        }
                        if (dy > max_dy)
                        {
                            dy = max_dy;
                        }

                        if (keypad_diamond[dy,dx] == '0')
                        {
                            dx += undo_dx;
                            dy += undo_dy;
                        }
                    }
                    code.Add(keypad[y, x]);
                    code_diamond.Add(keypad_diamond[dy, dx]);
                }
            }

            Console.WriteLine($"2016 Day 02 Part 1: {string.Join("", code)}");
            Console.WriteLine($"2016 Day 02 Part 2: {string.Join("", code_diamond)}");
        }
    }
}
