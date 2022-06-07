use std::collections::HashSet;

fn isHappy(mut n: i32) -> bool {
    let mut s: HashSet<i32> = HashSet::new();

    while n > 1 {
        if s.contains(&n) {
            return false;
        }

        let mut temp = 0;
        s.insert(n);
        while n > 0 {
            temp += i32::pow(n % 10, 2);
            n /= 10;
        }
        n = temp;
    }
    return true;
}

fn main() {
    println!("{}", isHappy(19));
    println!("{}", isHappy(2));
}
