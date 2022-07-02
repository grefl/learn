fn max_area(height: Vec<i32>) -> i32 {
    let mut left = 0;
    let mut right = height.len() - 1;
    let mut max_water: i32 = 0;

    while left < right {
        let min_height = i32::min(height[left], height[right]);
        let calc = min_height * (right - left) as i32;
        max_water = i32::max(max_water, calc);
        if height[left] <= height[right] {
            left += 1;
        } else {
            right -= 1
        }
    }
    return max_water;
}
#[cfg(test)]

mod test {
    use super::*;

    #[test]
    fn test_1() {
        // INPUT
        let height = vec![1, 8, 6, 2, 5, 4, 8, 3, 7];
        // OUTPUT
        let res = max_area(height);

        let should_equal = 49;
        assert_eq!(res, should_equal);
    }
}

fn main() {}
