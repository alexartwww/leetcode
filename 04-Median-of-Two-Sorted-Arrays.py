class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        return 0.0

if __name__ == '__main__':
    solution = Solution()
    assert solution.findMedianSortedArrays([1, 3], [2]) == 2
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert solution.findMedianSortedArrays([0, 0], [0, 0]) == 0
    assert solution.findMedianSortedArrays([], [1]) == 1
    assert solution.findMedianSortedArrays([2], []) == 2
