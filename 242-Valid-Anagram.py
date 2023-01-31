import time


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        d = {}

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in d:
                return False
            else:
                d[t[i]] -= 1

        for _, num in d.items():
            if num != 0:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()


    start = time.time()
    result = solution.isAnagram("anagram", "nagaram")
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == True

    start = time.time()
    result = solution.isAnagram("rat", "car")
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == False

