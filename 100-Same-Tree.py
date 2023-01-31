import time

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        if p.val != q.val:
            return False
        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right, q.right):
            return False
        return True


if __name__ == '__main__':
    solution = Solution()

    a_3 = TreeNode(3)
    a_2 = TreeNode(2)
    a_1 = TreeNode(1, a_2, a_3)

    b_3 = TreeNode(3)
    b_2 = TreeNode(2)
    b_1 = TreeNode(1, b_2, b_3)

    start = time.time()
    result = solution.isSameTree(a_1, b_1)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == True

    a_2 = TreeNode(2)
    a_1 = TreeNode(1, a_2, None)

    b_2 = TreeNode(2)
    b_1 = TreeNode(1, None, b_2)

    start = time.time()
    result = solution.isSameTree(a_1, b_1)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == False

