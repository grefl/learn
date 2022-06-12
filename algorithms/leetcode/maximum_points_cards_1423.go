package main

import "fmt"




func maxScore(cardPoints []int, k int) int {
  max := 0 
  for i := 0; i < k; i +=1 {
      max += cardPoints[i] 
  }
  curr := max
  for i := 0; i < k; i +=1 {
   curr -= cardPoints[k-i -1] 
   curr += cardPoints[len(cardPoints)-i -1]
   if curr > max {
     max = curr
   }

  }
  return max
}



func main() {

  fmt.Println(maxScore([]int{1,2,3,4,5,6,1}, 3))

}
