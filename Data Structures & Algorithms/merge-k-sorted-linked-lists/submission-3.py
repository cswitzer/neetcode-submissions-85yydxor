# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node: ListNode):
        self.node = node
    
    def __lt__(self, other: NodeWrapper):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        dummy = curr = ListNode(0)
        min_heap = []

        for l in lists:
            if l is not None:
                heapq.heappush(min_heap, NodeWrapper(l))
        
        while min_heap:
            node_wrapper = heapq.heappop(min_heap)
            curr.next = node_wrapper.node
            curr = curr.next

            if node_wrapper.node.next:
                heapq.heappush(min_heap, NodeWrapper(node_wrapper.node.next))
        
        return dummy.next
        

