class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        nums = []
        i = 0
        step = 1
        while i < len(s):
            if i+1 < len(s):
                if s[i:i+2] in romans:
                    nums.append(romans[s[i:i+2]])
                    step = 2
                else:
                    nums.append(romans[s[i]])
                    step = 1
            else:
                nums.append(romans[s[i]])
                step = 1
            i += step
        return sum(nums)

if __name__ == '__main__':
    solution = Solution()
    assert solution.romanToInt('III') == 3
    assert solution.romanToInt('IV') == 4
    assert solution.romanToInt('IX') == 9
    assert solution.romanToInt('LVIII') == 58
    assert solution.romanToInt('MCMXCIV') == 1994
