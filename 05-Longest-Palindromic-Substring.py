# leetcode: https://leetcode.com/problems/longest-palindromic-substring/

# Эта задача — одна из самых популярных на Medium уровне. Она проверяет твое понимание симметрии
# и умение оптимизировать перебор.

# Условие задачи (на русском):
# Дана строка 's'. Нужно найти самую длинную подстроку,
# которая является палиндромом (читается одинаково слева направо и наоборот).
#
# Пример 1: s = "babad" -> "bab" (или "aba")
# Пример 2: s = "cbbd" -> "bb"
#
# -----------------------------------------------------------------------------
# Алгоритм решения: Расширение из центра
#
# Идея:
# Вместо того чтобы проверять все подстроки, мы возьмем каждый символ
# (или промежуток между символами) за "центр" и будем расширяться в обе стороны,
# пока символы слева и справа равны.
#
# Почему два вида центров?
# 1. Нечетный палиндром: Центр — один символ (например, "aba", центр "b").
# 2. Четный палиндром: Центр — между двумя символами (например, "abba", центр "bb").
#
# 1. Создаем функцию-помощник expand(left, right), которая:
#    - Пока границы в пределах строки и s[left] == s[right]:
#    - Расширяет границы.
#    - Возвращает найденную подстроку-палиндром.
#
# 2. Основной цикл:
#    - Проходим по строке и для каждого индекса вызываем expand дважды:
#      для нечетной длины (i, i) и для четной (i, i+1).
#    - Сохраняем самую длинную из найденных подстрок.

class Solution:
    def longestPalindrome(self, s):
        res = ""

        def expand(l, r):
            # Расширяемся, пока символы равны
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # Возвращаем найденный палиндром
            # (l+1 и r, так как цикл остановился на несовпадающих индексах)
            return s[l + 1:r]

        for i in range(len(s)):
            # Вариант 1: нечетный (например, "aba")
            p1 = expand(i, i)
            if len(p1) > len(res):
                res = p1

            # Вариант 2: четный (например, "abba")
            p2 = expand(i, i + 1)
            if len(p2) > len(res):
                res = p2

        return res


if __name__ == '__main__':
    solution = Solution()

    s = "babad"
    result = solution.longestPalindrome(s)
    print(result)
    assert result == "bab"

    s = "cbbd"
    result = solution.longestPalindrome(s)
    print(result)
    assert result == "bb"

    s = "a"
    result = solution.longestPalindrome(s)
    print(result)
    assert result == "a"

    s = "ac"
    result = solution.longestPalindrome(s)
    print(result)
    assert result == "a"

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    result = solution.longestPalindrome(s)
    print(result)
    assert result == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
