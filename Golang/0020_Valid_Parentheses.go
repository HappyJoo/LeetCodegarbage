// reference: https://leetcode-cn.com/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode-solution/
// stack
// TIME： O(N)
// SPACE: O(N)

func isValid(s string) bool {
	n := len(s)
	if n%2 == 1 {
		return false
	}

	pairs := map[byte]byte{
		')': '(',
		'}': '{',
		']': '[',
	}
	stack := []byte{}

	for i := 0; i < n; i++ {
		if pairs[s[i]] > 0 {
			if len(stack) == 0 || pairs[s[i]] != stack[len(stack)-1] {
				return false
			}
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, s[i])
		}
	}
	return len(stack) == 0
}

// brute
// very inefficient
func isValid(s string) bool {
	n := len(s)
	if n%2 == 1 {
		return false
	}

	for {
		old := len(s)
		s = strings.Replace(s, "()", "")
		s = strings.Replace(s, "{}", "")
		s = strings.Replace(s, "[]", "")
		n = len(s)
		if s == "" {
			return true
		}
		if n == old {
			return false
		}
	}
}