fn maxScore(cardPoints: Vec<i32>, k: i32) -> i32 {
    let mut max: i32 = cardPoints[..k as usize].iter().sum::<i32>();

    let mut curr: i32 = max;
    for i in 0..k as usize {
        curr -= cardPoints[k as usize - i - 1];
        curr += cardPoints[cardPoints.len() - i - 1];
        if curr > max {
            max = curr;
        }
    }
    return max;
}

fn main() {
    println!("{}", maxScore(vec![1, 2, 3, 4, 5, 6, 1], 3));
}
