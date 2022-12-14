import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def merge2Lists(self, S1, S2):
        if S1 is None:
            return S2
        if S2 is None:
            return S1
        if S1.val <= S2.val:
            result = S1
            result.next = self.merge2Lists(S1.next, S2)
        else:
            result = S2
            result.next = self.merge2Lists(S1, S2.next)
        return result

    def mergeKLists(self, S):
        if len(S) == 0:
            return None

        result = None
        for node in S:
            result = self.merge2Lists(result, node)

        return result

if __name__ == '__main__':
    a = ListNode(5)
    b = ListNode(4, a)
    c = ListNode(1, b)

    x = ListNode(4)
    y = ListNode(3, x)
    z = ListNode(1, y)

    k = ListNode(6)
    l = ListNode(2, k)

    solution = Solution()
    start = time.time()
    result = solution.mergeKLists([])
    print(result, '{:.4f}'.format(time.time() - start))
    # assert result == [1, 1, 2, 3, 4, 4, 5, 6]
