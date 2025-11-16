# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return ListNode 
        # Floyd: slow, fast - if exist
        # if cycle: slow, head - entry
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                # mathematical proof: distance(head → entry) = distance(meeting point → entry)
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
        
        return None

# Let:
# a = distance from head to cycle entry
# b = distance from entry to meeting point
# c = length of the cycle
# k = number of full cycles slow has completed before meeting fast

# At the meeting:
# slow has walked: a + b + k*c
# fast has walked: 2(a + b + k*c)

# fast must be ahead of slow by exactly n full cycles:
# 2(a + b + k*c) - (a + b + k*c) = n*c
# => a + b = n*c

# Therefore:
# a = (n*c) - b

# Meaning:
# from meeting point, walking (c - b) steps reaches the entry
# and from head, walking a steps also reaches the entry
# => both pointers meet at the cycle entry