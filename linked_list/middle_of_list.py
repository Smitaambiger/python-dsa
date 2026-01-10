class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

# Test
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
print(middle_node(head))
