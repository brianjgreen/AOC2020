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
            string filePath = "../../data/2019/day02.dat";

            List<int> locations = [];

            using (StreamReader reader = new(filePath))
            {
                string? line;
                while ((line = reader.ReadLine()) != null)
                {
                    locations = Regex.Matches(line, @"\d+")
                                    .Select(m => int.Parse(m.Value))
                                    .ToList();
                }
            }

            List<int> orig_locations = locations.ToList();

            // replace position 1 with the value 12 and replace position 2 with the value 2
            locations[1] = 12;
            locations[2] = 2;

            int output_loc_0 = Run_program(locations);

            bool found_output = false;
            int noun_verb_100 = 0;
            int expected_output = 19690720;
            for (int noun = 0; noun < 100; noun++)
            {
                for (int verb = 0; verb < 100; verb++)
                {
                    if (!found_output)
                    {
                        locations = orig_locations.ToList();
                        locations[1] = noun;
                        locations[2] = verb;
                        int loc_0 = Run_program(locations);

                        if (loc_0 == expected_output)
                        {
                            noun_verb_100 = (100 * noun) + verb;
                            found_output = true;
                        }
                    }
                }
            }

            Console.WriteLine($"2019 Day 02 Part 1: {output_loc_0}");
            Console.WriteLine($"2019 Day 02 Part 2: {noun_verb_100}");
        }

        static int Run_program(List<int> locations)
        {
            bool active = true;
            int ip = 0;

            while (active)
            {
                switch(locations[ip])
                {
                    case 99:
                        active = false;
                        break;
                    case 1:
                        locations[locations [ip + 3]] = locations[locations[ip + 1]] + locations[locations[ip + 2]];
                        break;
                    case 2:
                        locations[locations [ip + 3]] = locations[locations[ip + 1]] * locations[locations[ip + 2]];
                        break;
                    default:
                        Console.WriteLine($"BAD INSTRUCTION ip={ip} val={locations[ip]}");
                        break;
                }

                ip += 4;
            }

            return locations[0];
        }
    }
}
