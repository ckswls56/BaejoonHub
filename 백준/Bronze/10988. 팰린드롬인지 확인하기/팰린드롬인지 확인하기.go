package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func isPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	text = strings.TrimSpace(text)

	if isPalindrome(text) {
		fmt.Println(1)
	} else {
		fmt.Println(0)
	}
}
