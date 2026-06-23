# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow represents the last node of the first list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow.next is the head of the second list
        # initially set slow.next to None since the head will now be the tail
        curr = slow.next
        prev = slow.next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # Now, we just interleave the two lists starting at list1
        # Loop through list2 since it is always equal or 1 shorter than the length of list1
        list1, list2 = head, prev
        while list2:
            next1, next2 = list1.next, list2.next
            list1.next = list2
            list2.next = next1
            list1, list2 = next1, next2

        