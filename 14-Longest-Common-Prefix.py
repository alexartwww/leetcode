class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            new_prefix = ''
            for i in range(1, len(s) + 1):
                if prefix[0:i] == s[0:i]:
                    new_prefix = prefix[0:i]
                else:
                    break
            if new_prefix != '':
                prefix = new_prefix
            else:
                return ''
        return prefix

if __name__ == '__main__':
    solution = Solution()
    assert solution.longestCommonPrefix(["ab","a"]) == 'a'
    assert solution.longestCommonPrefix(["flower","flow","flight"]) == 'fl'
    assert solution.longestCommonPrefix(["dog","racecar","car"]) == ''
