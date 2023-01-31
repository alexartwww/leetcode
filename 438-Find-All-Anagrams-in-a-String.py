import time
from collections import Counter


class Solution1:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        result = []
        countp = Counter(list(p))

        for i in range(len(s) - len(p) + 1):
            counts = Counter(list(s[i:i+len(p)]))
            flag = True
            for letter, num in counts.items():
                if letter not in countp:
                    flag = False
                    break
                if num > countp[letter]:
                    flag = False
                    break
            if flag:
                result.append(i)
        return result


class Solution2:
    def findAnagrams(self, s, p):
        result = []
        p = sorted(p)

        for i in range(len(s) - len(p) + 1):
            if sorted(s[i:i + len(p)]) == p:
                result.append(i)
        return result

class Solution3:
    def findAnagrams(self, a, b):
        if len(b) > len(a):  # If len of b is more than len of a, then there could be no anagram of b in a
            return []

        count_a = {}  # Hash map for count of a
        count_b = {}  # Hash map for count of b

        for i in range(len(b)):  # Storing frequency of characters for length of b
            count_a[a[i]] += 1
            count_b[b[i]] += 1

        if count_a == count_b:  # A specific case where we add the first index if matched
            ans = [0]
        else:
            ans = []

        sliding_left = 0  # We declare the sliding window pointer
        for right in range(len(b), len(a)):
            count_a[a[right]] += 1
            count_a[a[sliding_left]] -= 1

            if count_a[a[sliding_left]] == 0:
                count_a.pop(a[sliding_left])

            sliding_left = sliding_left + 1
            if count_a == count_b:
                ans.append(
                    sliding_left)  # If all the characters from b with their respective frequency are found at this index, we append.

        return ans

class Solution4:
    def findAnagrams(self, s, p):
        alphabet = set(s) | set(p)
        bitmap = {letter: 1 << i * 26 for i, letter in enumerate(alphabet)}

        result = []
        hashP = sum(bitmap[letter] for letter in p)
        for i in range(len(s) - len(p) + 1):
            hash = sum(bitmap[letter] for letter in s[i:i+len(p)])
            if hashP - hash == 0:
                result.append(i)

        return result


class Solution5:
    def findAnagrams(self, s, p):
        all_letters = set(s) | set(p)
        bitmap = {letter: 1 << i for i, letter in enumerate(all_letters)}

        hash0 = sum(bitmap[letter] for letter in s[:len(p)])
        current = hash0 - sum(bitmap[letter] for letter in p)
        result = []
        if current == 0:
            result.append(0)

        for i in range(len(s) - len(p)):
            letter_out = s[i]
            letter_in = s[i + len(p)]
            current = current + bitmap[letter_in] - bitmap[letter_out]
            if current == 0:
                result.append(i + 1)

        return result


if __name__ == '__main__':
    solution = Solution5()

    start = time.time()
    result = solution.findAnagrams("abcdcab", "ca")
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [4]

    start = time.time()
    result = solution.findAnagrams("cbaebabacdefghijklmnopqrstuvwxyz", "abc")
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [0, 6]

    start = time.time()
    result = solution.findAnagrams("abab", "ab")
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [0, 1, 2]
