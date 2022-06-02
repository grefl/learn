package main

import "fmt"

type Set struct {
  m map[int]bool
}
func set() *Set {
  s := &Set{make(map[int]bool)} 
  return s
}

func (s *Set) add(v int)  {
   _, ok := s.m[v]
   if !ok {
    s.m[v] = true 
   }
}
func (s *Set) in(v int) bool {
  _, ok := s.m[v]
  if ok {
    return true
   }
   return false
}

func contains_duplicate(input []int) bool {
  s := set() 

  for _, v := range input {
    if s.in(v) {
      return true
    }
    s.add(v)
  }
  return false
}
func contains_duplicate_simple(input []int) bool {
  
  m := make(map[int]bool)
  for _, v := range input {
    if _, ok := m[v]; ok {
      return true
    }
    m[v] = true
  }
  return false
}
func main() {
  input := []int{1,2,3,1}
  res := contains_duplicate(input)
  res_2 := contains_duplicate_simple(input)
  fmt.Println(res)
  fmt.Println(res_2)
}


