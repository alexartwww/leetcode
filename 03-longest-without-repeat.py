class Solution:
    def testStringUnique(self, s: str):
        l = len(s)
        for i in range(0, l):
            for j in range(i+1, l):
                if s[i] == s[j]:
                    return False
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        hop = 1
        l = len(s)
        i = 0
        while i < l:
            j = i + hop
            while j <= l:
                if self.testStringUnique(s[i:j]):
                    if j - i > result:
                        result = j - i
                        hop = result
                else:
                    break
                j += 1
            i += 1
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("dvdfdvdfdvdfdvdfdvdf"))
