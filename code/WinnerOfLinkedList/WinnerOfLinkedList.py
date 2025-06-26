# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        oddPts = 0
        evenPts = 0

        even = head
        odd = head.next

        while True:
            if odd.val > even.val:
                oddPts += 1
            else:
                evenPts += 1
            if odd.next == None:
                break
            odd = odd.next.next
            even = even.next.next
        
        if oddPts > evenPts:
            return "Odd"
        elif oddPts < evenPts:
            return "Even"
        else:
            return "Tie"