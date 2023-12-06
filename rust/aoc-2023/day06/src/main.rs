// Advent of Code 2023 - Day 6
// Rust solution: 6 Dec 2023 Brian Green
//
// Problem 1: What do you get if you multiply these numbers together?
// Problem 2: How many ways can you beat the record in this one much longer race?

// Return the product of the number of winning possibilities from each game
fn prod_games_won(game_stats: &Vec<u64>) -> u64 {
    let mut i: usize = 0;
    let mut total_prod: u64 = 1;
    while i < game_stats.len() {
        let game_time: u64 = game_stats[i];
        let game_distance: u64 = game_stats[i + 1];
        let mut winners: u64 = 0;
        for j in 1..game_time + 1 {
            if (game_time - j) * j > game_distance {
                winners += 1;
            }
        }
        total_prod *= winners;
        i += 2
    }
    total_prod
}

fn main() -> std::io::Result<()> {
    // Test Data Part 1
    // Time:      7  15   30
    // Distance:  9  40  200
    // Part 1
    let game_stats: Vec<u64> = vec![7, 9, 15, 40, 30, 200]; // Update with your puzzle input
    println!("Part 1 = {}", prod_games_won(&game_stats));
    //
    // Test Data Part 2
    // Time:      71530
    // Distance:  940200
    // Part 2
    let long_game_stats: Vec<u64> = vec![71530, 940200]; // Update with your puzzle input
    println!("Part 2 = {}", prod_games_won(&long_game_stats));
    Ok(())
}
