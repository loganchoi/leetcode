# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        stack = []

        while head:
            if head.val not in nums:
                if stack:
                    stack[-1].next = head
                stack.append(head)
            else:
                if stack:
                    stack[-1].next = None
            head = head.next
        
        return stack[0]