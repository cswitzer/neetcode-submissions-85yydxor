# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rev_k(self, head: Optional[ListNode], k: int):
        """
        return new_head, new_tail, next_head
        """
        prev = None
        curr = head
        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # after reversal
        # prev => new_head
        # head => new_tail
        # curr => next_head
        return prev, head, curr

    def has_k_nodes(self, head: Optional[ListNode], k: int) -> False:
        if not head:
            return False
        
        while head and k > 0:
            head = head.next
            k -= 1
        
        return k == 0

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prev_tail = ListNode(0, head)
        curr = head
        while self.has_k_nodes(curr, k):
            new_head, new_tail, next_head = self.rev_k(curr, k)
            # reset prev_tail.next to the new head to correct...
            prev_tail.next = new_head
            # ...this line here, where we set the new_tail's next value to old head
            new_tail.next = next_head
            prev_tail = new_tail
            
            curr = next_head
        return dummy.next
            