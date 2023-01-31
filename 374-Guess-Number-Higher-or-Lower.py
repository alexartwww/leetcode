import time


pick = 0
def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    return 0


class Solution:

    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while True:
            center = left + ((right - left) // 2)
            g = guess(center)
            if g == -1:
                right = center-1
            elif g == 1:
                left = center+1
            else:
                return center
            if right - left <= 1:
                break
        if guess(left) == 0:
            return left
        if guess(right) == 0:
            return right
        return -1


if __name__ == '__main__':
    solution = Solution()

    start = time.time()
    pick = 6
    result = solution.guessNumber(10)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 6

    start = time.time()
    pick = 2
    result = solution.guessNumber(2)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 2
