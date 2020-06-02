# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        current = head
        previous = None
        while current is not None:
            if current.val == val:
                if previous is None:
                    head = current.next
                else:
                    previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next
        return head


class WorseSolution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        current = previous = head
        while current is not None:
            if current.val == val:
                if current == head:
                    previous = current = head = current.next
                else:
                    previous.next = current.next
                    current = current.next
            else:
                previous = current
                current = current.next
        return head


class SentinelTwoPointersSolution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(val=0, next=head)
        prev, curr = sentinel, head
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next


class FinalSolution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(val=0, next=head)
        prev = sentinel
        while prev.next is not None:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return sentinel.next
