import heapq
import time
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        result = [0 for _ in range(k)]
        for i in range(k):
            max = 0
            for key in d:
                if d[key] > max:
                    max = d[key]
                    result[i] = key
            del d[result[i]]

        return result


class Solution2:
    def topKFrequent(self, nums, k):
        counts = Counter(nums)
        heap = []
        for key, count in counts.items():
            heapq.heappush(heap, [-count, key])

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


if __name__ == '__main__':
    solution = Solution2()

    start = time.time()
    result = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [1, 2]

    start = time.time()
    result = solution.topKFrequent([1], 1)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [1]
