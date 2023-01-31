import time

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDepth(self, node, depth):
        if node is None:
            return depth
        left_depth = self.getDepth(node.left, depth + 1)
        right_depth = self.getDepth(node.right, depth + 1)
        if left_depth == -1 or right_depth == -1:
            return -1
        if abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth)

    def isBalanced(self, root):
        if self.getDepth(root, 0) == -1:
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

