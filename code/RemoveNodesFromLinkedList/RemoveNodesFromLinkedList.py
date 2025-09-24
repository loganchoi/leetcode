# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        validStack = [head.val]
        i = 0
        head = head.next
        while head:
            if head.val <= validStack[-1]:
                validStack.append(head.val)
            else:
                while validStack and validStack[-1] < head.val:
                    validStack.pop()
                validStack.append(head.val)
            head = head.next

        newHead = ListNode()
        ans = newHead
        for val in validStack:
            newNode = ListNode(val)
            newHead.next = newNode
            newHead = newHead.next
        
        return ans.next
