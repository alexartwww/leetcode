import time


class Solution:
    def partitionLabels(self, S):
        ans = []
        m = {s: i for i, s in enumerate(S)}

        l, r = 0, 0

        for i, s in enumerate(S):
            r = max(r, m[s])
            if i == r:
                ans.append(r - l + 1)
                l = r + 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    start = time.time()
    result = solution.partitionLabels("qabcabcabc123xyz")
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [1, 9, 1, 1, 1, 1, 1, 1]
    start = time.time()
    result = solution.partitionLabels("ababcbacadefegdehijhklij")
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [9, 7, 8]
    start = time.time()
    result = solution.partitionLabels("eccbbbbdec")
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [10]
    start = time.time()
    result = solution.partitionLabels("caedbdedda")
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [1,9]
# ababcbacadefegdehijhklij