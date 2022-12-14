import time


class Solution(object):
    def groupAnagrams(self, strs):
        result = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key in result:
                result[key].append(word)
            else:
                result[key] = [word]
        return [result[key] for key in result]

if __name__ == '__main__':
    solution = Solution()
    start = time.time()
    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    start = time.time()
    result = solution.groupAnagrams([""])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[""]]
    start = time.time()
    result = solution.groupAnagrams(["a"])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [["a"]]
