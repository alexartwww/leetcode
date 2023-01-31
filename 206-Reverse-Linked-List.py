import time
from __init__ import ListNode


class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        window = [head, head.next, head.next.next]
        window[0].next = None

        while True:
            window[1].next = window[0]
            if window[-1] is not None:
                window.append(window[-1].next)
            else:
                return window[1]
            window = window[1:]


if __name__ == '__main__':
    solution = Solution()

    start = time.time()
    linked_list = ListNode(1).append_to_tail(2).append_to_tail(3).append_to_tail(4).append_to_tail(5).append_to_tail(6)
    linked_list = solution.reverseList(linked_list)

    print(linked_list)
