# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # l1, l2 同时走，val更小的接在merged上
        # one list is finished, "merged“ + the other list remainings
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val<=list2.val:
                cur.next = list1 # link
                # move
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 or list2
        return dummy.next
        # O(n);O(1)