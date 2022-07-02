fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
    if obstacle_grid[0][0] == 1 {
        return 0;
    }
    let rows = obstacle_grid.len();
    let cols = obstacle_grid[0].len();
    let mut num_ways = vec![vec![0; cols]; rows];
    let starting_value = {
        if obstacle_grid[0][0] == 1 {
            -1
        } else {
            1
        }
    };
    num_ways[0][0] = starting_value;

    for row in 1..rows {
        if obstacle_grid[row][0] == 1 || num_ways[row - 1][0] == -1 {
            num_ways[row][0] = -1;
        } else {
            num_ways[row][0] = 1;
        }
    }
    for col in 1..cols {
        if obstacle_grid[0][col] == 1 || num_ways[0][col - 1] == -1 {
            num_ways[0][col] = -1;
        } else {
            num_ways[0][col] = 1;
        }
    }

    for row in 1..rows {
        for col in 1..cols {
            if obstacle_grid[row][col] == 1
                || (num_ways[row - 1][col] == -1 && num_ways[row][col - 1] == -1)
            {
                num_ways[row][col] = -1;
            } else if num_ways[row - 1][col] == -1 {
                num_ways[row][col] = num_ways[row][col - 1];
            } else if num_ways[row][col - 1] == -1 {
                num_ways[row][col] = num_ways[row - 1][col];
            } else {
                num_ways[row][col] = num_ways[row - 1][col] + num_ways[row][col - 1];
            }
        }
    }
    let result = num_ways[rows - 1][cols - 1];
    if result > 0 {
        return result;
    }
    return 0;
}

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let should_be = 2;
        let obstacle_grid = vec![vec![0, 0, 0], vec![0, 1, 0], vec![0, 0, 0]];
        let actual = unique_paths_with_obstacles(obstacle_grid);
        assert_eq!(should_be, actual);
    }
    #[test]
    fn test_2() {
        let should_be = 0;
        let obstacle_grid = vec![vec![0, 0, 0], vec![1, 1, 1], vec![0, 0, 0]];
        let actual = unique_paths_with_obstacles(obstacle_grid);
        assert_eq!(should_be, actual);
    }
}
