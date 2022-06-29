struct Basket {
    one: i32,
    two: i32,
}
fn the_same2(basket: &mut Basket, fruit: i32) -> bool {
    if basket.one == fruit {
        return true;
    } else if basket.two == fruit {
        return true;
    }
    return false;
}

fn the_same(basket: &mut [i32], fruit: i32) -> bool {
    if basket[0] == fruit {
        return true;
    } else if basket[1] == fruit {
        return true;
    }
    return false;
}
fn total_fruit(fruits: Vec<i32>) -> i32 {
    if fruits.len() == 0 {
        return 0;
    }
    let mut start = 0;
    let mut max_fruits = 0;
    let mut basket: [i32; 2] = [0; 2];
    basket[0] = fruits[0];
    let mut index = 1;
    while index < fruits.len() {
        if fruits[index] != fruits[index - 1] {
            break;
        }
        index += 1;
    }
    // assign fruit to second basket
    if fruits.len() == index {
        return index as i32;
    }

    basket[1] = fruits[index];

    //return early if we have reached the end of the array

    if fruits.len() - 1 == index {
        return (index - start + 1) as i32;
    }

    for (index, fruit) in fruits.iter().enumerate() {
        if !the_same(&mut basket, *fruit) {
            basket[0] = *fruit;
            basket[1] = fruits[(index - 1) as usize];
            max_fruits = i32::max(max_fruits, (index - start) as i32);
            start = index - 1;
            while fruits[start] == fruits[(start - 1) as usize] {
                start -= 1;
            }
        } else {
            max_fruits = i32::max(max_fruits, (index - start + 1) as i32);
        }
    }
    return max_fruits;
}
fn total_fruit2(fruits: Vec<i32>) -> i32 {
    if fruits.len() == 0 {
        return 0;
    }
    let mut start = 0;
    let mut max_fruits = 0;
    let mut basket = Basket { one: 0, two: 0 };
    basket.one = fruits[0];
    let mut index = 1;
    while index < fruits.len() {
        if fruits[index] != fruits[index - 1] {
            break;
        }
        index += 1;
    }
    // assign fruit to second basket
    if fruits.len() == index {
        return index as i32;
    }

    basket.two = fruits[index];

    //return early if we have reached the end of the array

    if fruits.len() - 1 == index {
        return (index - start + 1) as i32;
    }

    for (index, fruit) in fruits.iter().enumerate() {
        if !the_same2(&mut basket, *fruit) {
            basket.one = *fruit;
            basket.two = fruits[(index - 1) as usize];
            max_fruits = i32::max(max_fruits, (index - start) as i32);
            start = index - 1;
            while fruits[start] == fruits[(start - 1) as usize] {
                start -= 1;
            }
        } else {
            max_fruits = i32::max(max_fruits, (index - start + 1) as i32);
        }
    }
    return max_fruits;
}
fn main() {
    let fruits = vec![1, 2, 1];
    let res = total_fruit2(fruits);
    println!("{}", res);
}
