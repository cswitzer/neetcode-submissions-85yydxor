# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge_two_lists(self, list1: ListNode | None, list2: ListNode | None):
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = list3 = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                list3.next = list1
                list3 = list1
                list1 = list1.next
            else:
                list3.next = list2
                list3 = list2
                list2 = list2.next
        if list1:
            list3.next = list1
        else:
            list3.next = list2
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        for i in range(len(lists) - 1):
            list1 = lists[i]
            list2 = lists[i + 1]
            list3 = self.merge_two_lists(list1, list2)
            lists[i + 1] = list3
        return lists[-1]

