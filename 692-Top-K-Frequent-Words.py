import heapq
import time
from collections import Counter


class Solution:
    def topKFrequent(self, words, k):
        counts = Counter(words)

        heap = []
        for key, count in counts.items():
            heapq.heappush(heap, [-count, key])

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


if __name__ == '__main__':
    solution = Solution()

    start = time.time()
    result = solution.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == ["i", "love"]

    start = time.time()
    result = solution.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == ["the", "is", "sunny", "day"]
