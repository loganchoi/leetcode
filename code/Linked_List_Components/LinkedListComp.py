# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)


        total = 0
        node = head
        while node:
            if node.val in nums:
                total += 1
                while node.val in nums:
                    node = node.next
                    if node == None:
                        return total
            else:
                node = node.next
        
        return total