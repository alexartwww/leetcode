import time


class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while True:
            center = left + ((right - left) // 2)
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right
            if target == nums[center]:
                return center
            if right - left <= 2:
                break
            if target < nums[center]:
                right = center
            if target > nums[center]:
                left = center
        return -1


if __name__ == '__main__':
    solution = Solution()

    start = time.time()
    result = solution.search([-1, 0, 3, 5, 9, 12], 9)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 4

    start = time.time()
    result = solution.search([-1, 0, 3, 5, 9, 12], 2)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == -1
