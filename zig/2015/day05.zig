const std = @import("std");

fn containsAny(haystack: []const u8) bool {
    const needle_list = [_][]const u8{ "ab", "cd", "pq", "xy" };
    for (needle_list) |needle| {
        // std.mem.count returns the number of occurrences.
        // If it's greater than 0, the substring is found.
        if (std.mem.count(u8, haystack, needle) > 0) {
            return true; // Found at least one match
        }
    }
    return false; // No matches found after checking all needles
}

fn pairAppearsTwice(s: []const u8) bool {
    const len = s.len;

    if (len < 4) return false; // minimum needed for a repeated non-overlapping pair

    // For each pair s[i..i+2]
    for (s, 0..) |_, i| {
        if (i + 1 >= len) break;

        const a = s[i];
        const b = s[i + 1];

        // Search the remainder starting at i+2
        var j: usize = i + 2;
        while (j + 1 < len) {
            if (s[j] == a and s[j + 1] == b) {
                return true;
            }
            j += 1;
        }
    }

    return false;
}

fn repeatWithGap(s: []const u8) bool {
    const len = s.len;

    if (len < 3) return false; // minimum needed for a repeated character with a gap

    // For each character s[i]
    for (s, 0..) |_, i| {
        if (i + 2 >= len) break;

        const a = s[i];
        const c = s[i + 2];

        if (a == c) {
            return true;
        }
    }

    return false;
}

pub fn main() !void {
    // 1. Get a handle to the current working directory.
    const cwd = std.fs.cwd();

    // 2. Open the file in the current working directory.
    const file = try cwd.openFile("../../data/2015/day05.dat", .{});
    defer file.close();

    // 3. Create a GeneralPurposeAllocator instance.
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer {
        const leak_check = gpa.deinit();
        if (leak_check == .leak) {
            std.debug.print("Memory leak detected!\n", .{});
        }
    }
    const allocator = gpa.allocator();

    // 4. Read the entire file into an allocated buffer (new Zig 0.15.x API).
    const file_contents = try file.readToEndAlloc(allocator, std.math.maxInt(usize));
    defer allocator.free(file_contents);

    var it = std.mem.splitScalar(u8, file_contents, '\n');
    var nice_count_part1: usize = 0;
    var nice_count_part2: usize = 0;

    while (it.next()) |line| {
        if (line.len == 0) continue; // skip empty lines

        // Part 1: Check for at least 3 vowels, at least one letter that appears twice in a row, and does not contain "ab", "cd", "pq", or "xy".
        var vowel_count: usize = 0;
        var has_double = false;
        for (line, 0..) |ch, idx| {
            if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u') {
                vowel_count += 1;
            }
            if (idx > 0 and ch == line[idx - 1]) {
                has_double = true;
            }
        }
        const is_nice_part1 = vowel_count >= 3 and has_double and !containsAny(line);
        if (is_nice_part1) {
            nice_count_part1 += 1;
        }
        const is_nice_part2 = pairAppearsTwice(line) and repeatWithGap(line);
        if (is_nice_part2) {
            nice_count_part2 += 1;
        }
    }

    std.debug.print("Nice count (Part 1): {}\n", .{nice_count_part1});
    std.debug.print("Nice count (Part 2): {}\n", .{nice_count_part2});
}
