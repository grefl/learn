package main
import "fmt"
func sum(nums []int) int {
  s := 0
  for _, num := range nums {
    s +=num
  }
  return s
}
func max(a, b int) int {
  if a > b {
    return a
  }
  return b
}
func findMaxAverage(nums []int, k int) float64 {
  max_sum := sum(nums[0:k])
  current_sum := max_sum
  left := 1
  right := k 
  for right < len(nums) {
    current_sum = current_sum - nums[left-1] + nums[right]
    max_sum = max(current_sum, max_sum)
    left +=1
    right +=1
  }
  return float64(max_sum) / float64(k)
}
func main() {

  fmt.Println(findMaxAverage([]int{1,12,-5,-6,50,3}, 4))
}
