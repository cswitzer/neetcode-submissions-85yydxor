# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow is now the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # start from head and prev and merge the two
        curr1, curr2 = head, prev
        while curr2.next:
            temp1, temp2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = temp1
            curr1, curr2 = temp1, temp2
        