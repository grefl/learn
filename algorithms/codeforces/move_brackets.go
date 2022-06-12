package main

import (
	"bufio"
	"fmt"
	"os"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func move_brackets() {
	s := bufio.NewScanner(os.Stdin)
	brackets := make([]string, 0)
	output := make([]int, 0)

	i := 0

	for s.Scan() {
		if i%2 == 0 && i != 0 {
			brackets = append(brackets, s.Text())
		}
		i += 1
	}
	for _, bracket := range brackets {
		i := 0
		left := 0
		right := 0
		count := 0
		for i < len(bracket) {
			if bracket[i] == '(' {
				left += 1
			} else if bracket[i] == ')' {
				right += 1
				if left < right {
					count = max(right-left, count)
				}
			}
			i += 1
		}
		output = append(output, count)
	}
	for _, count := range output {
		fmt.Println(count)
	}
}
func main() {

	move_brackets()

}
