using System;
using System.IO;
using System.Linq;
using System.Net;
using System.Text.RegularExpressions;


namespace Day03
{
    class Program
    {
        static void Main(string[] args)
        {
            string filePath = "../../data/2016/day03.dat";

            List<int> triangles = [];
            List<int> alpha = [0, 0, 0];
            List<int> beta = [0, 0, 0];
            List<int> charlie = [0, 0, 0];
            int row = 0;
            int possible = 0;
            int rot_possible = 0;

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    triangles = Regex.Matches(line, @"\d+")
                                    .Select(m => int.Parse(m.Value))
                                    .ToList();

                    if ((triangles[0] + triangles[1] > triangles[2]) &&
                        (triangles[1] + triangles[2] > triangles[0]) &&
                        (triangles[2] + triangles[0] > triangles[1]))
                    {
                        possible++;
                    }

                    alpha[row % 3] = triangles[0];
                    beta[row % 3] = triangles[1];
                    charlie[row % 3] = triangles[2];

                    if (row % 3 == 2)
                    {
                        if ((alpha[0] + alpha[1] > alpha[2]) &&
                            (alpha[1] + alpha[2] > alpha[0]) &&
                            (alpha[2] + alpha[0] > alpha[1]))
                        {
                            rot_possible++;
                        }

                        if ((beta[0] + beta[1] > beta[2]) &&
                            (beta[1] + beta[2] > beta[0]) &&
                            (beta[2] + beta[0] > beta[1]))
                        {
                            rot_possible++;
                        }

                        if ((charlie[0] + charlie[1] > charlie[2]) &&
                            (charlie[1] + charlie[2] > charlie[0]) &&
                            (charlie[2] + charlie[0] > charlie[1]))
                        {
                            rot_possible++;
                        }

                    }

                    row++;
                }
            }

            Console.WriteLine($"2016 Day 03 Part 1: {possible}");
            Console.WriteLine($"2016 Day 03 Part 2: {rot_possible}");
        }
    }
}
