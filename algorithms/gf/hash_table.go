package main

import (
	"fmt"
	"log"
	"os"
  "time"
	"strings"
)

func bench(compute func(), count int) {
  for i := 0; i < count; i +=1 {
    start := time.Now()
    compute()
    t := time.Now()
    elapsed := t.Sub(start)
    fmt.Println(elapsed)
    fmt.Println(count)
  }
}

const S uint = 7
const P uint = 31

func take(array []string, amount int) []string {
	new_array := make([]string, amount)
	for i := 0; i < amount; i += 1 {
		new_array[i] = array[i]
	}
	return new_array
}
func (h *HashTable) hash(key string) uint {
	hashed_key := S
	for _, c := range key {
    hashed_key += ((hashed_key * 31) + uint(c)) % uint(len(h.array))
	}
  return hashed_key % uint(len(h.array))
}

type HashTable struct {
	array    [][]string
	capacity uint
}

func (h *HashTable) size() int {
	return len(h.array)
}

func (h *HashTable) insert(current_key, current_value string) bool {
	hashed_index := h.hash(current_key)
	for len(h.array[hashed_index]) == 0 {
		hashed_index = (hashed_index + 1) % uint(len(h.array))
	}
	h.array[hashed_index][0] = current_key
	h.array[hashed_index][1] = current_value
	return true
}

func (h *HashTable) get(current_key string) (string, bool) {
	hashed_index := h.hash(current_key)
	for len(h.array[hashed_index]) == 0 {
    hashed_index = (hashed_index + 1) % uint(len(h.array))
	}
	if h.array[hashed_index][0] == current_key {
		return h.array[hashed_index][1], true
	}
	return "", false
}

func test(words []string) {


	// words_100 := take(words, 100000)
  array := make([][]string, len(words)*2)
	for i, _ := range array {
		array[i] = make([]string, 2)
	}
	h := HashTable{array: array, capacity: 0}
	fmt.Println(h.size())
  h.insert("gorb", "me")
	h.insert("GORB!", "I am GORB!")
  for _, word := range words {
		h.insert(word, word)
	}
  res, ok := h.get("gorb")
	if !ok {
		log.Fatal("couldn't find key")
	}
  people, ok := h.get("people")
	if !ok {
		log.Fatal("couldn't find key")
	}
	fmt.Println(res)
  fmt.Println(people)
}
func main() {
  data, err := os.ReadFile("./words.txt")
  if err != nil {
    log.Fatal(err)
  }
  words := strings.Split(string(data), "\n")
  bench( func() {test(words)}, 10)
}
