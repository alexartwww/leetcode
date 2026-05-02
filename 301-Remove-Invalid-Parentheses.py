import time


class Solution:
    def getWrong(self, s, reverse=False):
        close = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        open = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        if not reverse:
            forth = open
            back = close
        else:
            forth = close
            back = open
        wrong = []
        stack = []
        for i in range(len(s)):
            if not reverse:
                index = i
            else:
                index = len(s) - i - 1
            symbol = s[index]
            if symbol not in back and symbol not in forth:
                continue
            if symbol in back:
                if stack:
                    if (s[stack[-1]] != back[symbol]):
                        wrong.append(index)
                        continue
                    else:
                        stack.pop()
                else:
                    wrong.append(index)
                    continue
            if symbol in forth:
                stack.append(index)
        if stack:
            wrong = wrong + stack

        return wrong

    def getReversed(self, s):
        repl = {
            ')': '(',
            ']': '[',
            '}': '{',
            '(': ')',
            '[': ']',
            '{': '}',
        }
        result = ''
        for symbol in s:
            if symbol in repl:
                result += repl[symbol]
            else:
                result += symbol
        return result

    def removeInvalidParentheses(self, s):
        # result = []
        wrong = self.getWrong(s, True)
        if len(wrong) == len(s):
            return []
        result = []
        sr = ""

        for i, symbol in enumerate(s):
            if i not in wrong:
                sr += symbol
        result.append(sr)
        # for i in wrong:
        #     head = s[:i+1]
        #     tail = s[i+1:]
        #     rs = self.removeInvalidParentheses(self.getReversed(head))
        #     for r in rs:
        #         result.append(self.getReversed(r)+tail)
        return result


if __name__ == '__main__':
    solution = Solution()

    start = time.time()
    result = solution.removeInvalidParentheses("()())")
    print(result, '{:.4f}'.format(time.time() - start))
    # assert result == ["(())()", "()()()"]
    # #
    # start = time.time()
    # result = solution.removeInvalidParentheses("(a)())()")
    # print(result, '{:.4f}'.format(time.time() - start))
    # # assert result == ["(a())()", "(a)()()"]
    # #
    # start = time.time()
    # result = solution.removeInvalidParentheses(")(")
    # print(result, '{:.4f}'.format(time.time() - start))
    # # assert result == [""]
