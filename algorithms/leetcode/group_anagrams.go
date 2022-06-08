package main
import (
        "fmt"
        "sort"
       )

type RuneSlice []rune

func (p RuneSlice) Len() int           { return len(p) }
func (p RuneSlice) Less(i, j int) bool { return p[i] < p[j] }
func (p RuneSlice) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }

func sorted(s string) string {
    runes := []rune(s)
    sort.Sort(RuneSlice(runes))
    return string(runes)
}

func group_anagrams(strs []string) [[]string] {
  m = make(map[string][]string)
  for s := range strs {
   sorted_s = sorted(s) 
  }
}
func main() {
  str := "asdf" 
  fmt.Println(sorted(str))
}
