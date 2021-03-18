// slow fast pointer
// TIME： O(N)
// SPACE: O(1)
func hasCycle(head *ListNode) bool {
    slow := &ListNode{0, head}
    fast := &ListNode{0, head}
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next 
        if slow == fast {
            return true
        }
    }
    return false
}


// hash table
// TIME： O(N)
// SPACE: O(N)
func hasCycle(head *ListNode) bool {
    seen := map[*ListNode]struct{}{}
    for head != nil {
        if _, ok := seen[head]; ok {
            return true
        }
        seen[head] = struct{}{}
        head = head.Next
    }
    return false
}
