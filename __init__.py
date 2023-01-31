class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append_to_tail(self, val):
        self.get_tail().next = ListNode(val)
        return self

    def get_tail(self):
        current = self

        while current.next is not None:
            current = current.next

        return current

    def __str__(self):
        result = []
        current = self

        while current.next is not None:
            result.append(current.val)
            current = current.next

        result.append(current.val)
        return ' -> '.join([str(i) for i in result])


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
