const std = @import("std");

pub fn main() !void {
    const cwd = std.fs.cwd();
    const file = try cwd.openFile("../../data/2015/day04.dat", .{});
    defer file.close();

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var secret = try file.readToEndAlloc(allocator, std.math.maxInt(usize));
    defer allocator.free(secret);

    // Trim trailing newline if present
    if (secret.len > 0 and secret[secret.len - 1] == '\n') {
        secret = secret[0 .. secret.len - 1];
    }

    var counter: usize = 0;
    var found_five = false;
    var found_six = false;

    // Reusable buffer for "secret + counter"
    var buf: [128]u8 = undefined;

    while (!found_five or !found_six) {
        const input = try std.fmt.bufPrint(&buf, "{s}{d}", .{ secret, counter });

        // MD5 must be reinitialized each iteration
        var md5 = std.crypto.hash.Md5.init(.{});
        md5.update(input);

        var digest: [16]u8 = undefined;
        md5.final(&digest);

        // Part 1: 5 leading hex zeros
        if (!found_five and digest[0] == 0 and digest[1] == 0 and digest[2] < 0x10) {
            std.debug.print("Part 1: {d}\n", .{counter});
            found_five = true;
        }

        // Part 2: 6 leading hex zeros
        if (!found_six and digest[0] == 0 and digest[1] == 0 and digest[2] == 0) {
            std.debug.print("Part 2: {d}\n", .{counter});
            found_six = true;
        }

        counter += 1;
    }
}
