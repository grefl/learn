use std::collections::HashMap;
fn can_construct(ransom_note: String, magazine: String) -> bool {
    /*
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
    Each letter in magazine can only be used once in ransomNote.

    Example 1:
    =======================================
    Input: ransomNote = "a", magazine = "b"
    Output: false
    =======================================
    */

    let mut map: HashMap<char, i32> = HashMap::new();

    for c in magazine.chars() {
        if let Some(ch) = map.get_mut(&c) {
            *ch += 1;
        } else {
            map.insert(c, 1);
        }
    }
    for c in ransom_note.chars() {
        if let Some(ch) = map.get_mut(&c) {
            *ch -= 1;
            if *ch < 0 {
                return false;
            }
        } else {
            return false;
        }
    }
    return true;
}

fn main() {
    let ransom_note = String::from("aa");
    let magazine = String::from("ab");

    let can = can_construct(ransom_note, magazine);
    println!("{}", can);
}
