fn sum(nums: Vec<i32>) -> i32 {
    let mut s = 0;
    for num in nums.iter() {
        s += num;
    }
    return s;
}
fn max(a: i32, b: i32) -> i32 {
    if a > b {
        return a;
    }
    return b;
}

fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
    let mut max_sum = sum(nums[0..k as usize].to_vec());
    let mut current_sum = max_sum;
    let mut left: usize = 1;
    let mut right: usize = k as usize;

    while right < nums.len() {
        current_sum = current_sum - nums[left - 1] + nums[right];
        max_sum = max(current_sum, max_sum);
        left += 1;
        right += 1;
    }
    return max_sum as f64 / k as f64;
}
fn main() {
    let res = find_max_average(vec![1, 12, -5, -6, 50, 3], 4);
    println!("{}", res);
}
