class Solution:
    def isPalindrome(self, x: int) -> bool:
        if not((-2)**31 <= x and x <= 2**31 - 1):
            return False

        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.isPalindrome(121) == True
    assert solution.isPalindrome(-121) == False
    assert solution.isPalindrome(10) == False
    assert solution.isPalindrome(-101) == False
