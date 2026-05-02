# leetcode: https://leetcode.com/problems/reverse-words-in-a-string/

# Принимая на вход строку s, измените порядок слов на обратный.
#
# Слово определяется как последовательность символов, отличных от пробела.
# Слова в строке s должны быть разделены как минимум одним пробелом.
#
# Возвращает строку слов в обратном порядке, объединенных одним пробелом.
#
# Обратите внимание, что строка s может содержать пробелы в начале или конце, или несколько пробелов между
# двумя словами. Возвращаемая строка должна содержать только один пробел, разделяющий слова. Не добавляйте
# лишних пробелов.

class Solution(object):
    def reverseWords(self, s):
        words = []
        current_word = ""
        for i in range(len(s)):
            if s[i] != " ":
                current_word = current_word + s[i]
            elif current_word != "":
                words.append(current_word)
                current_word = ""
        if current_word != "":
            words.append(current_word)
        words.reverse()
        return " ".join(words)

class Solution2(object):
    def reverseWords(self, s):
        # s.strip() убирает пробелы по краям
        # split() без аргументов делит по любому количеству пробелов
        list_s = s.strip().split()
        n = len(list_s)

        l = 0
        r = n - 1

        # Классический инверс массива
        while l < r:
            list_s[l], list_s[r] = list_s[r], list_s[l]
            l += 1
            r -= 1

        return ' '.join(list_s)


if __name__ == '__main__':
    solution = Solution2()

    s = "the sky is blue"
    result = solution.reverseWords(s)
    print(result)
    assert result == "blue is sky the"

    s = "  hello world  "
    result = solution.reverseWords(s)
    print(result)
    assert result == "world hello"

    s = "a good   example"
    result = solution.reverseWords(s)
    print(result)
    assert result == "example good a"
