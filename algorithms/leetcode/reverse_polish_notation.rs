fn helper<T>(stack: &mut Vec<T>) -> (T, T, &mut Vec<T>) {
    assert!(stack.len() >= 2);
    let op1 = stack.pop().unwrap();
    let op2 = stack.pop().unwrap();
    return (op1, op2, stack);
}
fn eval_rpn(tokens: Vec<String>) -> i32 {
    let mut stack = vec![];
    for token in tokens {
        match token.as_str() {
            "+" => {
                assert!(stack.len() >= 2);
                let (op1, op2, stack) = helper(&mut stack);
                stack.push(op2 + op1);
            }
            "-" => {
                assert!(stack.len() >= 2);
                let (op1, op2, stack) = helper(&mut stack);
                stack.push(op2 - op1);
            }
            "*" => {
                assert!(stack.len() >= 2);
                let (op1, op2, stack) = helper(&mut stack);
                stack.push(op1 * op2);
            }
            "/" => {
                assert!(stack.len() >= 2);
                let (op1, op2, stack) = helper(&mut stack);
                stack.push(op2 / op1);
            }
            _ => stack.push(token.parse::<i32>().unwrap()),
        }
    }
    return stack.pop().unwrap();
}
fn main() {
    let tokens = vec![
        "10".to_string(),
        "6".to_string(),
        "9".to_string(),
        "3".to_string(),
        "+".to_string(),
        "-11".to_string(),
        "*".to_string(),
        "/".to_string(),
        "*".to_string(),
        "17".to_string(),
        "+".to_string(),
        "5".to_string(),
        "+".to_string(),
    ];
    let res = eval_rpn(tokens);
    println!("{}", res);
}
