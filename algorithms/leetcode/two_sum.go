package main
import "fmt"

func twoSum(nums []int, target int) []int {
  m := make(map[int]int, len(nums))    

  for i, n := range nums {
    if _, ok := m[n]; ok {
      return []int{i, m[n]}
    }
    diff := target - n
    m[diff] = i
  }
  return []int{-1, -1}
}

func main() {
  nums := []int{2,7, 11, 23} 
  target := 9
  fmt.Println(twoSum(nums, target))

}
