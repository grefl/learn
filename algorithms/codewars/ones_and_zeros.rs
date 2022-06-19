fn binary_slice_to_number(slice: &[u32]) -> u32 {
    // your code here
    let length = slice.len() - 1;
    let mut decimal_num = 0;
    for (idx, &num) in slice.iter().enumerate() {
        let power: u32 = (length - idx) as u32;
        if num == 1 {
            decimal_num += u32::pow(2, power);
        }
    }
    return decimal_num as u32;
}

fn main() {
    let number = binary_slice_to_number(&vec![0, 0, 1, 1]);
    println!("{}", number)
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_1() {
        assert_eq!(binary_slice_to_number(&vec![0, 0, 1, 1]), 3)
    }
}
