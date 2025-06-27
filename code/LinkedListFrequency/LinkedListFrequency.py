# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = {}

        node = head
        while node:
            count[node.val] = 1 + count.get(node.val,0)
            node = node.next

        ans = ListNode()
        curNode = ans
        for v in count.values():
            newNode = ListNode(v)
            curNode.next = newNode
            curNode = curNode.next
        
        return ans.next