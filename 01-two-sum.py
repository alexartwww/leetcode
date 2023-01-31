class Solution:
    def twoSum(self, nums, target):
        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums):
                if num_i + num_j == target and i != j:
                    return [i, j]
        return []


class Solution2:
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            if num not in d:
                d[num] = i
        return []


if __name__ == '__main__':
    solution = Solution2()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    assert solution.twoSum([-3, 4, 3, 90], 0) == [0, 2]
