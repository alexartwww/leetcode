class Solution:
    def myAtoi(self, s: str) -> int:
        return 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.myAtoi("42") == 42
    assert solution.myAtoi("   -42") == -42
    assert solution.myAtoi("4193 with words") == 4193
    assert solution.myAtoi("words and 987") == 0
    assert solution.myAtoi("-91283472332") == -2147483648
