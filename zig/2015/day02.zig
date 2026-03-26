const std = @import("std");

pub fn main() !void {
    // 1. Get a handle to the current working directory.
    const cwd = std.fs.cwd();

    // 2. Open the file in the current working directory.
    const file = try cwd.openFile("../../data/2015/day02.dat", .{});
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

    var total_area: u32 = 0;
    var total_ribbon: u32 = 0;
    var it = std.mem.splitScalar(u8, file_contents, '\n');

    while (it.next()) |line| {
        if (line.len == 0) continue; // skip empty lines

        var dims = std.mem.splitScalar(u8, line, 'x');

        const length_str = dims.next().?;
        const width_str = dims.next().?;
        const height_str = dims.next().?;

        const length = try std.fmt.parseInt(u32, length_str, 10);
        const width = try std.fmt.parseInt(u32, width_str, 10);
        const height = try std.fmt.parseInt(u32, height_str, 10);

        var smallest = length * width;
        total_area += 2 * smallest;
        var width_height = width * height;
        smallest = if (smallest < width_height) smallest else width_height;
        total_area += 2 * width_height;
        var height_length = height * length;
        smallest = if (smallest < height_length) smallest else height_length;
        total_area += 2 * height_length;
        total_area += smallest;

        smallest = 2 * length + 2 * width;
        width_height = 2 * width + 2 * height;
        smallest = if (smallest < width_height) smallest else width_height;
        height_length = 2 * height + 2 * length;
        smallest = if (smallest < height_length) smallest else height_length;
        total_ribbon += length * width * height;
        total_ribbon += smallest;
    }

    std.debug.print("Total area: {d}\n", .{total_area});
    std.debug.print("Total ribbon: {d}\n", .{total_ribbon});
}
