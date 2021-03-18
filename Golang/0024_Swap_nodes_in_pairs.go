// iteration
func swapPairs(head *ListNode) *ListNode {
    dummyHead := &ListNode{0, head}
    temp := dummyHead

    for temp.Next != nil && temp.Next.Next != nil {
        one := temp.Next
        two := temp.Next.Next
        temp.Next = two
        one.Next = two.Next
        two.Next = one
        temp = one
    }
    return dummyHead.Next
}


// recursive
func swapPairs(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head 
    }
    newHead := head.Next
    head.Next = swapPairs(newHead.Next)
    newHead.Next = head
    return newHead
}
