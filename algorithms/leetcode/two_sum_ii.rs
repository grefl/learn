fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    /*

    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
    Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space.



    Example 1:

    ==========================================================================================
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
    ==========================================================================================

    */

    let mut left = 0;
    let mut right = numbers.len() - 1;

    while left < right {
        let sum = numbers[left] + numbers[right];
        if sum == target {
            return vec![left as i32 + 1, right as i32 + 1];
        } else if sum < target {
            left += 1;
        } else {
            right -= 1;
        }
    }
    return vec![-1, -1];
}

fn main() {
    let numbers = vec![2, 7, 11, 15];
    let target = 9;
    let indexes = two_sum(numbers, target);
    println!("{:#?}", indexes);
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let numbers = vec![2, 7, 11, 15];
        let target = 9;

        let indexes = two_sum(numbers, target);
        let should_equal = vec![1, 2];
        assert_eq!(indexes, should_equal);
    }

    #[test]
    fn test_2() {
        let numbers = vec![22, 7, 11, 15];
        let target = 9;

        let indexes = two_sum(numbers, target);
        let should_equal = vec![-1, -1];
        assert_eq!(indexes, should_equal);
    }
}
