# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tempList = ListNode(0)
        head = tempList

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tempList.next = l1
                l1 = l1.next
            else:
                tempList.next = l2
                l2 = l2.next
            tempList = tempList.next
        if l1 == None:
            tempList.next = l2
        else:
            tempList.next = l1

        return head.next


a = ListNode(2)
a1 = ListNode(3)
a.next = a1
b = ListNode(1)
b1 = ListNode(1)
b.next = b1

print(Solution().mergeTwoLists(a, b))
