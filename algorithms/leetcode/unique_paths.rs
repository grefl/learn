fn unique_paths(m: i32, n: i32) -> i32 {
    let mut num_ways: Vec<Vec<i32>> = vec![vec![0; n as usize]; m as usize];
    num_ways[0][0] = 1;

    for j in 1..(n as usize) {
        num_ways[0][j] = 1;
    }

    for i in 1..(m as usize) {
        num_ways[i][0] = 1;
    }

    for i in 1..(m as usize) {
        for j in 1..(n as usize) {
            num_ways[i][j] = num_ways[i][j - 1] + num_ways[i - 1][j];
        }
    }

    return num_ways[(m - 1) as usize][(n - 1) as usize];
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let actual = unique_paths(3, 7);
        let should_be = 28;
        assert_eq!(actual, should_be);
    }
}
fn main() {}
