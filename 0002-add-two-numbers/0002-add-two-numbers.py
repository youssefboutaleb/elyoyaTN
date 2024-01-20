# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        head=ListNode(0)
        curr=head
        while l1 or l2 or carry:
            if l1 :
                val1=l1.val 
                l1=l1.next
            else :
                val1=0
            if l2 :
                val2=l2.val 
                l2=l2.next
            else :
                val2=0
            
            res=val1+val2+carry
            carry=res//10
            res=res%10
            newNode = ListNode(res % 10)
            curr.next = newNode
            curr = newNode
            
        return head.next
