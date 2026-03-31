# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1
        
        l3 = curr = ListNode(0)
        carry = 0
        while l1 and l2:
            sum_val = l1.val + l2.val + carry
            if sum_val >= 10:
                sum_val, new_carry = sum_val - 10, 1
            else:
                new_carry = 0
            
            sum_node = ListNode(sum_val)
            curr.next = sum_node
            curr = sum_node
            l1, l2 = l1.next, l2.next
            carry = new_carry

        while l1:
            new_sum = l1.val + carry
            sum_node = ListNode(new_sum)
            if new_sum >= 10:
                sum_node = ListNode(new_sum - 10)
                carry = 1
            else:
                carry = 0
            curr.next = sum_node
            curr = sum_node
            l1 = l1.next
        while l2:
            new_sum = l2.val + carry
            print(new_sum)
            sum_node = ListNode(new_sum)
            if new_sum >= 10:
                sum_node = ListNode(new_sum - 10)
                carry = 1
            else:
                carry = 0
            curr.next = sum_node
            curr = sum_node
            l2 = l2.next
        
        # final edge case. If the carry over is still 1, then we need to add 1
        # to the final sum
        if carry == 1:
            curr.next = ListNode(1)

        return l3.next
