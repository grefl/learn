use std::collections::HashMap;

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut m: HashMap<i32, i32> = HashMap::new();

    for (i, n) in nums.iter().enumerate() {
        if m.contains_key(n) {
            return vec![i as i32, *m.get(n).unwrap() as i32];
        }

        let diff: i32 = target - n;
        m.insert(diff, i as i32);
    }
    return vec![-1, -1];
}

fn main() {
    let nums = vec![2, 7, 12, 1];
    let target = 9;
    let res = two_sum(nums, target);
    println!("{:?}", res);
}
