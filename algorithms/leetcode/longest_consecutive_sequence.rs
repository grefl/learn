use std::collections::HashMap;

fn max(a: i32, b: i32) -> i32 {
    if a > b {
        return a;
    }
    b
}

fn longest_consecutive_sequence(nums: Vec<i32>) -> i32 {
    if nums.len() == 0 {
        return 0;
    }
    let mut map: HashMap<i32, bool> = HashMap::new();

    for num in nums.iter() {
        if map.contains_key(num) {
            continue;
        }
        map.insert(*num, true);
    }
    let mut max_sequence = 0;
    let values: Vec<i32> = map.clone().into_iter().map(|(key, _val)| key).collect();
    for num in values {
        let mut mini_max = 1;
        let mut copy = num.clone();
        if map.contains_key(&(&copy - 1)) {
            continue;
        }
        copy += 1;
        loop {
            if map.contains_key(&copy) {
                mini_max += 1;
                copy += 1;
            } else {
                max_sequence = max(mini_max, max_sequence);
                break;
            }
        }
    }
    return max_sequence;
}

fn main() {
    let res = longest_consecutive_sequence(vec![100, 1, 200, 2, 3, 4]);
    println!("{}", res);
}
