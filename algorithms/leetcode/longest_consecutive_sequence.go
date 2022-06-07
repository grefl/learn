package main
import "fmt"

func max(a, b int) int {
  if a > b {
    return a
  }
  return b
}

func longest_consecutive_sequence(numbers []int) int {
  if len(numbers) == 0 {
    return 0
  }
  m := make(map[int]bool, len(numbers))
  for _, number := range numbers {
    if _, ok := m[number]; ok {
      continue
    }
    m[number] = true
  }
  max_sequence := 1
  for number := range m {
    mini_max := 1 
    if _, ok := m[number-1]; ok {
      continue
    }
    for {
      number +=1
      if _, ok := m[number]; ok {
        mini_max +=1 
      } else {
        max_sequence = max(max_sequence, mini_max)
        break
      }
    }
  }
  return max_sequence 
}

func main() {
  nums := []int{100, 4, 200, 1, 3, 2} 
  fmt.Println(longest_consecutive_sequence(nums))

}
