package main
import (
  "fmt"
  "math"
  )


func is_happy(n int) bool {
  m := make(map[int]bool) 

  for n > 1 {
    if _, ok := m[n]; ok {
      return false
    }
    m[n] = true
    var temp int = 0 
    for n > 0 {
      temp += int(math.Pow(float64(n % 10), float64(2)))
      n /= 10
    }
    n = temp
  }
  return true 
}

func main() {

  fmt.Println(is_happy(19))
  fmt.Println(is_happy(2))
}
