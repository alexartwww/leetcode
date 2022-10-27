class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        number = []
        sign = None
        for char in s:
            if sign == None and len(number) == 0 and char in [' ']:
                continue
            if sign == None and len(number) == 0 and char in ['+','-']:
                sign = 1 if char == '+' else -1
                continue
            if len(number) == 0 and char not in ['1','2','3','4','5','6','7','8','9','0']:
                break
            if char in ['1','2','3','4','5','6','7','8','9','0']:
                number.append(int(char))
                continue
            if len(number) > 0 and char not in ['1','2','3','4','5','6','7','8','9','0']:
                break
        number = number[::-1]
        for i, num in enumerate(number):
            result += num * pow(10, i)

        sign = 1 if sign == None else sign
        result = result * sign
        if result < (-1)*(2**31):
            result = (-1)*(2**31)
        if result > 2**31 - 1:
            result = 2**31 - 1

        return result
