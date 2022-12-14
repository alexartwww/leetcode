import time


class Solution(object):
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == '__main__':
    solution = Solution()

    start = time.time()
    result = solution.merge([[1, 4], [2, 3]])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[1,4]]
    start = time.time()
    result = solution.merge([[1,4],[0,0]])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[0,0],[1,4]]
    start = time.time()
    result = solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[1, 6], [8, 10], [15, 18]]
    start = time.time()
    result = solution.merge([[1, 4], [0, 1]])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[0, 4]]
    start = time.time()
    result = solution.merge([[1, 4], [4, 5]])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[1, 5]]
    start = time.time()
    result = solution.merge([[1, 4], [0, 4]])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[0, 4]]
