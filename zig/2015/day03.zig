const std = @import("std");

const Coord = struct {
    x: i32,
    y: i32,
};

pub fn main() !void {
    const cwd = std.fs.cwd();
    const file = try cwd.openFile("../../data/2015/day03.dat", .{});
    defer file.close();

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const file_contents = try file.readToEndAlloc(allocator, std.math.maxInt(usize));
    defer allocator.free(file_contents);

    var map = std.AutoHashMap(Coord, i32).init(allocator);
    defer map.deinit();
    var robo_map = std.AutoHashMap(Coord, i32).init(allocator);
    defer robo_map.deinit();

    var x: i32 = 0;
    var y: i32 = 0;
    var alt_x: i32 = 0;
    var alt_y: i32 = 0;
    var robo_x: i32 = 0;
    var robo_y: i32 = 0;
    var is_santa_turn: bool = true;

    // starting house
    try map.put(Coord{ .x = 0, .y = 0 }, 1);
    try robo_map.put(Coord{ .x = 0, .y = 0 }, 2);

    for (file_contents) |ch| {
        switch (ch) {
            '^' => {
                x += 1;
                if (is_santa_turn) alt_x += 1 else robo_x += 1;
            },
            'v' => {
                x -= 1;
                if (is_santa_turn) alt_x -= 1 else robo_x -= 1;
            },
            '>' => {
                y += 1;
                if (is_santa_turn) alt_y += 1 else robo_y += 1;
            },
            '<' => {
                y -= 1;
                if (is_santa_turn) alt_y -= 1 else robo_y -= 1;
            },
            else => continue,
        }

        const house = Coord{ .x = x, .y = y };
        const alt_house = Coord{ .x = alt_x, .y = alt_y };
        const robo_house = Coord{ .x = robo_x, .y = robo_y };

        const entry = try map.getOrPut(house);
        if (entry.found_existing) {
            entry.value_ptr.* += 1;
        } else {
            entry.value_ptr.* = 1;
        }

        if (is_santa_turn) {
            is_santa_turn = false;
            const alt_entry = try robo_map.getOrPut(alt_house);
            if (alt_entry.found_existing) {
                alt_entry.value_ptr.* += 1;
            } else {
                alt_entry.value_ptr.* = 1;
            }
        } else {
            is_santa_turn = true;
            const robo_entry = try robo_map.getOrPut(robo_house);
            if (robo_entry.found_existing) {
                robo_entry.value_ptr.* += 1;
            } else {
                robo_entry.value_ptr.* = 1;
            }
        }
    }

    std.debug.print("Unique houses visited: {d}\n", .{map.count()});
    std.debug.print("Unique houses visited with Robo-Santa: {d}\n", .{robo_map.count()});
}
