# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        validStack = [head]
        i = 0
        head = head.next
        while head:
            if head.val <= validStack[-1].val:
                validStack.append(head)
            else:
                while validStack and validStack[-1].val < head.val:
                    validStack.pop()
                if validStack:
                    validStack[-1].next = head
                validStack.append(head)
            head = head.next

        return validStack[0]