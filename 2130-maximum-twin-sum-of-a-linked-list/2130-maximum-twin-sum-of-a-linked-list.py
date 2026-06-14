# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        store = []

        while node.next:
            store.append(node.val)
            node = node.next

        store.append(node.val)
        n = len(store)

        for i in range((n//2), n):
            store[abs(i+1-n)] += store[i]

        return max(store)