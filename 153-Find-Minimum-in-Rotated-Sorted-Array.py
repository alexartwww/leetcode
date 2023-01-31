import time


class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums)-1
        while True:
            if right - left <= 1:
                return min(nums[left], nums[right])
            center = left + ((right - left) // 2)
            if nums[right] < nums[center]:
                left = center
            elif nums[left] > nums[center]:
                right = center
            else:
                right = center
        return -1

if __name__ == '__main__':
    solution = Solution()

    start = time.time()
    result = solution.findMin([3,4,5,1,2])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 1

    start = time.time()
    result = solution.findMin([4,5,6,7,0,1,2])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 0

    start = time.time()
    result = solution.findMin([11,13,15,17])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 11
