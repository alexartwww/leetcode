# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listNodeToList(l: ListNode):
    result = []
    while l != None:
        result.append(l.val)
        l = l.next
    return result

def listNodeToNum(l: ListNode):
    result = 0
    i = 0
    while l != None:
        result += l.val * pow(10, i)
        l = l.next
        i += 1
    return result


class Solution:
    def listNodeToNum(self, l: ListNode) -> int:
        result = 0
        i = 0
        while l != None:
            result += l.val * pow(10, i)
            l = l.next
            i += 1
        return result

    def numToListNode(self, num: int) -> ListNode:
        result = [ListNode(int(i)) for i in list(str(num))]
        for l in range(1, len(result)):
            result[l].next = result[l-1]
        return result[-1]

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.listNodeToNum(l1)
        num2 = self.listNodeToNum(l2)
        return self.numToListNode(num1 + num2)


if __name__ == '__main__':
    # Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
    # Output: [7, 0, 8]
    # Explanation: 342 + 465 = 807.

    a = ListNode(3)
    b = ListNode(4, a)
    c = ListNode(2, b)

    x = ListNode(4)
    y = ListNode(6, x)
    z = ListNode(5, y)

    k = ListNode(8)
    l = ListNode(0, k)
    m = ListNode(7, l)

    solution = Solution()
    res = solution.addTwoNumbers(c, z)

    print(solution.listNodeToNum(res))
    # print(listNodeToNum(res))
