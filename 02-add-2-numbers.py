from . import ListNode


class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        result = None
        current = None
        next_rank = 0
        while True:
            s = next_rank
            if l1 is not None:
                s += l1.val
                l1 = l1.next
            if l2 is not None:
                s += l2.val
                l2 = l2.next
            val = s if s < 10 else s % 10
            next_rank = 0 if s < 10 else s // 10
            if result is None:
                result = ListNode(val)
                current = result
            else:
                current.next = ListNode(val)
                current = current.next
            if l1 is None and l2 is None:
                if next_rank != 0:
                    current.next = ListNode(next_rank)
                break

        return result


if __name__ == '__main__':
    # Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
    # Output: [7, 0, 8]
    # Explanation: 342 + 465 = 807.

    a = ListNode(2).append_to_tail(4).append_to_tail(3)
    b = ListNode(5).append_to_tail(6).append_to_tail(4)

    solution = Solution()
    res = solution.addTwoNumbers(a, b)
    print(res)

    a = ListNode(9).append_to_tail(9).append_to_tail(9).append_to_tail(9).append_to_tail(9).append_to_tail(
        9).append_to_tail(9)
    b = ListNode(9).append_to_tail(9).append_to_tail(9).append_to_tail(9)
    solution = Solution()
    res = solution.addTwoNumbers(a, b)
    print(res)
