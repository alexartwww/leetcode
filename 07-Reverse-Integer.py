class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        result = int(str(x * sign)[::-1]) * sign
        if (-2)**31 <= result and result <= 2**31 - 1:
            return result
        else:
            return 0

if __name__ == '__main__':
    solution = Solution()
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(0) == 0
    assert solution.reverse(1534236469) == 0
