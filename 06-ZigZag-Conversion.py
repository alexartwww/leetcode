class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        output = []
        for i in range(numRows):
            line = []
            for j in range(len(s)):
                line.append(' ')
            output.append(line)
        for index, symbol in enumerate(s):
            if index % (2 * numRows - 2) < numRows:
                x = (index // (2 * numRows - 2)) * (numRows - 1)
                y = index % (2 * numRows - 2)
            else:
                x = (index // (2 * numRows - 2)) * (numRows - 1) + (index % (2 * numRows - 2) % numRows) + 1
                y = numRows - (index % (2 * numRows - 2) % numRows) - 2
            output[y][x] = symbol
        result = ''
        for line in output:
            result += ''.join(line)
        #     print(' '.join(line))
        return result.replace(' ', '')


if __name__ == '__main__':
    solution = Solution()
    assert solution.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    # P     I    N
    # A   L S  I G
    # Y A   H R
    # P     I
    assert solution.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    # P   A   H   N
    # A P L S I I G
    # Y   I   R
    assert solution.convert('A', 1) == 'A'
