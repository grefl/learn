fn valid_palindrome(s: String) -> bool {
    let mut left = 0;
    let mut right = s.len() - 1;
    let my_s: &[u8] = s
        .chars()
        .filter(|c| c.is_whitespace())
        .cloned()
        .collect::<String>()
        .as_bytes();
    while left < right && my_s[left] == my_s[right] {
        left += 1;
        right -= 1;
    }
    return left == right;
}
fn main() {
    let res = valid_palindrome(String::from("A man, a plan, a canal: Panama"));
    println!("{}", res);
}
