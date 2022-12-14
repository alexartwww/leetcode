import time


class Solution:
    def search(self, nums, target):
        if len(nums) == 0 \
                or len(nums) == 1 and nums[0] != target \
                or len(nums) == 2 and nums[0] != target and nums[1] != target \
                or len(nums) == 3 and nums[0] != target and nums[1] != target and nums[2] != target \
                :
            return -1
        elif len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 2 and nums[0] == target:
            return 0
        elif len(nums) == 2 and nums[1] == target:
            return 1
        elif len(nums) == 3 and nums[0] == target:
            return 0
        elif len(nums) == 3 and nums[1] == target:
            return 1
        elif len(nums) == 3 and nums[2] == target:
            return 2

        br = 0
        left = 0
        right = len(nums) - 1

        if nums[left] > nums[right]:
            while True:
                br = left + ((right - left) // 2)
                if nums[br] > nums[right]:
                    left = br
                else:
                    right = br
                if right - left == 1:
                    br = right
                    break

        if br == 0:
            left = 0
            right = len(nums) - 1
        elif target >= nums[0] and target <= nums[br - 1]:
            left = 0
            right = br - 1
        else:
            left = br
            right = len(nums) - 1

        while True:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if right - left <= 1:
                break
            br = left + ((right - left) // 2)
            if target > nums[br]:
                left = br
            else:
                right = br
        return -1


if __name__ == '__main__':
    solution = Solution()

    start = time.time()
    result = solution.search([4, 5, 6, 7, 0, 1, 2], 0)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 4
    #
    start = time.time()
    result = solution.search([4, 5, 6, 7, 0, 1, 2], 3)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == -1
    #
    start = time.time()
    result = solution.search([1], 0)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == -1
    #
    start = time.time()
    result = solution.search([4, 5, 6, 7, 0, 1, 2], 4)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 0
    #
    start = time.time()
    result = solution.search([4, 5, 6, 7, 8, 1, 3], 0)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == -1
    #
    start = time.time()
    result = solution.search([3, 4, 5, 6, 1, 2], 2)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 5
    #
    start = time.time()
    result = solution.search([2, 3, 5, 6, 8, 9, 0], 1)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == -1
