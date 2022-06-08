package main
import "fmt"


func canConstruct(ransomNote, magazine string) bool {
  m := make(map[rune]int)

  for _, letter := range magazine {
    if _, ok := m[letter]; !ok {
      m[letter] = 1 
    } else {
      m[letter] +=1 
    }

  }
  for _, letter := range ransomNote {
    if _, ok := m[letter]; !ok {
      return false 
    }
    m[letter] -=1
    if m[letter] < 0 {
      return false
    }
  }
  return true
}


func main() {
  
  fmt.Println(canConstruct("aa", "aab"))
  fmt.Println(canConstruct("aa", "ab"))

}
