fn max_profit(prices: Vec<i32>) -> i32 {
    let mut profit = 0;
    let mut min_price = std::i32::MAX;
    for price in prices {
        if price < min_price {
            min_price = price;
        } else if price > min_price {
            profit = std::cmp::max(profit, price - min_price);
        }
    }

    return profit;
}
fn main() {
    let prices = vec![7, 1, 5, 3, 6, 4];
    let profit = max_profit(prices);
    println!("{}", profit);
}
