import time
from . import ListNode


class Solution:
    def hasCycle(self, head) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while fast != None and fast.next != None and fast != slow:
            slow = slow.next
            fast = fast.next.next

        if fast is None or fast.next is None:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()

    start = time.time()
    linked_list = ListNode(1).append_to_tail(3).append_to_tail(4).append_to_tail(5).append_to_tail(6)
    result = solution.hasCycle(linked_list)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == False

    start = time.time()
    linked_list = ListNode(1).append_to_tail(3).append_to_tail(4).append_to_tail(5)
    result = solution.hasCycle(linked_list)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == False

    start = time.time()
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(6)
    head.next.next.next.next.next = head.next
    result = solution.hasCycle(head)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == True

