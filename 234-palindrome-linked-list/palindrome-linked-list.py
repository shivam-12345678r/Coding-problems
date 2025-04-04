# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #we have traversed till here
        #now we want to reverse thius linked list
        if fast:
            slow = slow.next
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        first,second = head,prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True

        
        