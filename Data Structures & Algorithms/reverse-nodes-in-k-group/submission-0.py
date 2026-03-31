# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        
        prev_group_tail = dummy
        curr = head

        while curr:
            if not self.has_k_nodes(curr, k):
                break
            
            # reverse k nodes
            new_head, new_tail, next_group = self.reverse_k(curr, k)

            # reconnect
            prev_group_tail.next = new_head
            new_tail.next = next_group

            # move pointers
            prev_group_tail = new_tail
            curr = next_group
        
        return dummy.next


    def has_k_nodes(self, node: Optional[ListNode], k: int) -> bool:
        if not node:
            return False
        
        while node and k > 0:
            node = node.next
            k -= 1
        
        return k == 0

    def reverse_k(self, head: Optional[ListNode], k: int):
        """
        Demonstration:
        dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
                 ^
                 |
                curr

        reverse the first group of k where k = 3
        None <- 1 <- 2 <- 3  4 -> 5 -> 6
                ^         ^  ^
                |         |  |
                |         | curr (next group start)
                |         |
                |        prev (new head)
                |
             head (new tail)
        """

        prev = None
        curr = head

        while k > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            k -= 1
        
        # prev is the new head
        # head is the new tail
        # curr is next group start
        return prev, head, curr

