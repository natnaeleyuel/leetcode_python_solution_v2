# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 1
        node = head

        while node.next:
            node = node.next
            n += 1
        
        store = []
        curr = head

        for i in range(n):
            if i <= (n / 2) - 1:
                store.append(curr.val)
            else:
                store[abs(i+1-n)] += curr.val

            if curr.next:
                curr = curr.next
        
        return max(store)
