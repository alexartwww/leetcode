class Solution:
    def search(self, nums, target) -> bool:
        # return target in nums
        # return target in set(nums)
        nums = list(set(nums))
        while True:
            if len(nums) == 0:
                return False
            if len(nums) == 1:
                return nums[0] == target
            if len(nums) == 2:
                return nums[0] == target or nums[1] == target

            middle = len(nums) // 2
            left = nums[:middle]
            right = nums[middle:]

            if left[0] <= left[-1] and target >= left[0] and target <= left[-1]:
                nums = left
            elif right[0] <= right[-1] and target >= right[0] and target <= right[-1]:
                nums = right
            elif left[0] > left[-1] and (target >= left[0] or target <= left[-1]):
                nums = left
            elif right[0] > right[-1] and (target >= right[0] or target <= right[-1]):
                nums = right
            else:
                return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.search([2, 5, 6, 0, 0, 1, 2], 0) == True
    assert solution.search([2, 5, 6, 0, 0, 1, 2], 3) == False
    assert solution.search([1, 0, 1, 1, 1], 0) == True
    assert solution.search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2) == True
    assert solution.search([1, 3, 5], 1) == True
