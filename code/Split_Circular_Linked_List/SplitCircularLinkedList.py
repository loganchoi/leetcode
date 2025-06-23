# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, linkedList: Optional[ListNode]) -> List[Optional[ListNode]]:
        if linkedList.next.next == linkedList:
            firstPtr = linkedList
            secondPtr = linkedList.next
            firstPtr.next = firstPtr
            secondPtr.next = secondPtr
            return [firstPtr,secondPtr]
        
        firstPtr = linkedList
        secondPtr = linkedList

        while secondPtr.next != linkedList and secondPtr.next.next != linkedList:
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next.next
        

        cycle2_head = firstPtr.next
        cycle1_head = linkedList

        firstPtr.next = cycle1_head

        if secondPtr.next.next == linkedList:
            secondPtr = secondPtr.next
        
        secondPtr.next = cycle2_head

        return [cycle1_head,cycle2_head]