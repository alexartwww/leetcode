class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height):
                if j > i and min(h1, h2) * (j - i) > result:
                    result = min(h1, h2) * (j - i)
        return result
