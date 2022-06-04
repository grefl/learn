package main

import "fmt"

func valid_anagram(s string, t string) bool {
	m := make(map[rune]int)
	if len(s) != len(t) {
		return false
	}
	for _, c := range s {
		if _, ok := m[c]; ok {
			m[c] += 1
		} else {
			m[c] = 1
		}
	}
	for _, c := range t {
		if _, ok := m[c]; !ok {
			return false
		}
		m[c] -= 1

		if m[c] < 0 {
			return false
		}

	}
	return true
}

func main() {
	s := "anagram"
	t := "nagaram"
	fmt.Println(valid_anagram(s, t))
}
