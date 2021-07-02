class Solution:
    def isValid(self, s: str) -> bool:
        back = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        forth = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        stack = []
        for symbol in s:
            if symbol in back:
                if stack:
                    if (stack[-1] != back[symbol]):
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            if symbol in forth:
                stack.append(symbol)
        return stack == []

if __name__ == '__main__':
    solution = Solution()
    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("(]") == False
    assert solution.isValid("([)]") == False
    assert solution.isValid("{[]}") == True
