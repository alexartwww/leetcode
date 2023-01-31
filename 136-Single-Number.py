import time


class Solution1:
    def singleNumber(self, nums) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                del d[i]
        return list(d.keys())[0]


class Solution2:
    def singleNumber(self, nums) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result


if __name__ == '__main__':
    solution = Solution2()

    start = time.time()
    result = solution.singleNumber([2, 2, 1])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 1

    start = time.time()
    result = solution.singleNumber([4, 1, 2, 1, 2])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 4

    start = time.time()
    result = solution.singleNumber([1])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 1
