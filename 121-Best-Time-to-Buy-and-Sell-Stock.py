import time


class Solution:
    def maxProfit(self, prices) -> int:
        return 0


if __name__ == '__main__':
    solution = Solution()


    start = time.time()
    result = solution.maxProfit([])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 0
