import heapq
import time
from collections import Counter


class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        if len(nums) == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return []
        print(len(nums))
        nums = sorted(nums)
        result = {}
        i = 0
        for a in range(0, len(nums) - 3, 1):
            for b in range(1, len(nums) - 2, 1):
                if b == a:
                    continue
                for c in range(2, len(nums) - 1, 1):
                    if c == a or c == b:
                        continue
                    for d in range(3, len(nums), 1):
                        if d == a or d == b or d == c:
                            continue
                        i += 1
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            key = ' '.join([str(i) for i in sorted([nums[a], nums[b], nums[c], nums[d]])])
                            result[key] = sorted([nums[a], nums[b], nums[c], nums[d]])
        print(i)
        return list(result.values())


class Solution2:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        if len(nums) == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return []
        i = 0
        result = {}
        sum_twos = {}
        counts = {}
        for a in range(0, len(nums), 1):
            if nums[a] not in counts:
                counts[nums[a]] = 1
            else:
                counts[nums[a]] += 1
            for b in range(0, len(nums), 1):
                if b == a:
                    continue
                i += 1
                if nums[a] + nums[b] not in sum_twos:
                    sum_twos[nums[a] + nums[b]] = [set([a, b])]
                else:
                    sum_twos[nums[a] + nums[b]].append(set([a, b]))
        for s, a_b_s in sum_twos.items():
            if target - s in sum_twos:
                for a_b in a_b_s:
                    for c_d in sum_twos[target - s]:
                        if a_b != c_d:
                            l_keys = list(a_b) + list(c_d)
                            l = sorted([nums[l_keys[0]], nums[l_keys[1]], nums[l_keys[2]], nums[l_keys[3]]])
                            cs = Counter(l)
                            flag = True
                            for n, c in cs.items():
                                if c > counts[n]:
                                    flag = False
                            if flag:
                                i += 1
                                key = ' '.join([str(i) for i in l])
                                result[key] = l
        print(i)
        return list(result.values())


class Solution3:
    def twoSum(self, nums, target):
        result = []
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d and d[target - nums[i]] > 0:
                d[target - nums[i]] -= 1
                result.append([nums[i], target - nums[i]])
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        return result

    def kSum(self, nums, target, k):
        result_all = []

        if k == 2:
            return self.twoSum(nums, target)

        for i in range(len(nums)):
            for subset in self.kSum(nums, target - nums[i], k - 1):
                result_all.append(subset + [nums[i]])

        return result_all

    def fourSum(self, nums, target):
        counts = Counter(nums)
        result = {}
        result_all = self.kSum(nums, target, 4)
        for subset in result_all:
            flag = True
            cs = Counter(subset)
            for num, c in cs.items():
                if counts[num] < c:
                    flag = False
                    break
            if flag:
                key = ' '.join(sorted([str(i) for i in subset]))
                result[key] = subset
        return list(result.values())

class Solution4:
    def twoSum(self, nums, target):
        res = []
        s = set()

        for i in range(len(nums)):
            if len(res) == 0 or res[-1][1] != nums[i]:
                if target - nums[i] in s:
                    res.append([target - nums[i], nums[i]])
            s.add(nums[i])

        return res

    def kSum(self, nums, target, k):
        result = []
        if not nums:
            return result

        average_value = target // k

        if average_value < nums[0] or nums[-1] < average_value:
            return result

        if k == 2:
            return self.twoSum(nums, target)

        for i in range(len(nums)):
            for subset in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                if i == 0 or nums[i - 1] != nums[i]:
                    result.append(subset + [nums[i]])

        return result

    def fourSum(self, nums, target):
        nums.sort()
        return self.kSum(nums, target, 4)


class SolutionN:
    def fourSum(self, nums, target):
        def twoSum(nums, target):
            res = []
            s = set()

            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])

            return res

        def kSum(nums, target, k):
            res = []

            # If we have run out of numbers to add, return res.
            if not nums:
                return res

            # There are k remaining values to add to the sum. The
            # average of these values is at least target // k.
            average_value = target // k

            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)

            return res


        nums.sort()
        return kSum(nums, target, 4)


if __name__ == '__main__':
    solution = Solution4()

    print(solution.fourSum([1, 2, 1, 3, 1, 2, 3, 4, 5, 6, 2, 7, 8, 9, 0, -2, -6, -4, -3], 7))


    start = time.time()
    result = solution.fourSum([1, 0, -1, 0, -2, 2], 0)
    print(result, '{:.4f}'.format(time.time() - start))
    # assert result == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    start = time.time()
    result = solution.fourSum([2, 2, 2, 2, 2], 8)
    print(result, '{:.4f}'.format(time.time() - start))
    # assert result == [[2, 2, 2, 2]]

    start = time.time()
    result = solution.fourSum(
        [-500, -481, -480, -469, -437, -423, -408, -403, -397, -381, -379, -377, -353, -347, -337, -327, -313, -307,
         -299, -278, -265, -258, -235, -227, -225, -193, -192, -177, -176, -173, -170, -164, -162, -157, -147, -118,
         -115, -83, -64, -46, -36, -35, -11, 0, 0, 33, 40, 51, 54, 74, 93, 101, 104, 105, 112, 112, 116, 129, 133, 146,
         152, 157, 158, 166, 177, 183, 186, 220, 263, 273, 320, 328, 332, 356, 357, 363, 372, 397, 399, 420, 422, 429,
         433, 451, 464, 484, 485, 498, 499], 2139)
    print(result, '{:.4f}'.format(time.time() - start))
    # assert result == []

    start = time.time()
    result = solution.fourSum(
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20,
         20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
         30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 50, 50, 50, 50,
         50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60,
         60, 60, 60, 60, 60, 60, 60, 60, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70,
         80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 90, 90, 90, 90, 90, 90, 90, 90,
         90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90], 200)
    print(result, '{:.4f}'.format(time.time() - start))
    # assert result == []
