# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2Lists(self, node1: Optional[ListNode], node2: Optional[ListNode]):
        if not node1:
            return node2
        elif not node2:
            return node1
        
        dummy = curr = ListNode(0)
        while node1 and node2:
            if node1.val <= node2.val:
                curr.next = node1
                curr = node1
                node1 = node1.next
            else:
                curr.next = node2
                curr = node2
                node2 = node2.next
        
        while node1:
            curr.next = node1
            curr = node1
            node1 = node1.next
        while node2:
            curr.next = node2
            curr = node2
            node2 = node2.next
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        if len(lists) == 1:
            first_list = lists[0]
            return first_list[0]
        
        # we can merge k lists by merge two lists at a time
        new_head = lists[0]
        for idx in range(len(lists) - 1):
            new_head = self.merge2Lists(new_head, lists[idx + 1])
        
        return new_head


