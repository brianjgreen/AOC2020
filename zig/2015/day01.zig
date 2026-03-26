const std = @import("std");

pub fn main() !void {
    // 1. Get a handle to the current working directory.
    const cwd = std.fs.cwd();

    // 2. Open the file in the current working directory.
    const file = try cwd.openFile("../../data/2015/day01.dat", .{});
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

    // 5. Print the contents.
    // std.debug.print("File contents:\n{s}\n", .{file_contents});

    var floor: i32 = 0;
    var position: usize = 0;
    var basement_position: usize = 0;

    for (file_contents) |ch| {
        position += 1;
        if (ch == '(') {
            floor += 1;
            // std.debug.print("index {d}: open paren\n", .{i});
        } else if (ch == ')') {
            floor -= 1;
            // std.debug.print("index {d}: close paren\n", .{i});
        }
        if (floor == -1 and basement_position == 0) {
            basement_position = position;
        }
    }

    std.debug.print("Final floor: {d}\n", .{floor});
    std.debug.print("Position of first basement visit: {d}\n", .{basement_position});
}
