# leetcode: https://leetcode.com/problems/string-to-integer-atoi/

# Эта задача проверяет не столько твои навыки в алгоритмах, сколько умение внимательно следовать спецификации
# и обрабатывать краевые случаи (edge cases). Основная сложность здесь — 32-битные ограничения
# и "грязные" входные данные.

# Условие задачи (на русском):
# Реализовать функцию myAtoi, которая переводит строку в 32-битное целое число.
# Правила:
# 1. Пропустить пробелы в начале.
# 2. Определить знак ('-' или '+'), если он есть.
# 3. Считать цифры до первого нецифрового символа.
# 4. Ограничить результат диапазоном [-2^31, 2^31 - 1].
#
# -----------------------------------------------------------------------------
# Алгоритм решения: Пошаговая обработка
#
# Идея: Просто идем по строке и применяем правила одно за другим.
#
# 1. Очистка: Используем .lstrip(), чтобы убрать пробелы в начале.
# 2. Знак: Проверяем первый символ. Если это '-' — запоминаем sign = -1.
# 3. Сбор числа: Итерируемся по оставшимся символам, пока это цифры.
#    Формула сборки: res = res * 10 + digit.
# 4. Переполнение: В конце проверяем, не вышли ли мы за границы 32-бит.
#
# -----------------------------------------------------------------------------

class Solution:
    def myAtoi(self, s):
        # 1. Удаляем пробелы
        s = s.lstrip()
        if not s:
            return 0

        # 2. Определяем знак
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        # 3. Читаем цифры
        res = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit
            i += 1

        # Применяем знак
        res *= sign

        # 4. Обработка переполнения (Clamping)
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX

        return res


if __name__ == '__main__':
    solution = Solution()

    s = "42"
    result = solution.myAtoi(s)
    print(result)
    assert result == 42

    s = "   -42"
    result = solution.myAtoi(s)
    print(result)
    assert result == -42

    s = "4193 with words"
    result = solution.myAtoi(s)
    print(result)
    assert result == 4193

    s = "words and 987"
    result = solution.myAtoi(s)
    print(result)
    assert result == 0

    s = "-91283472332"
    result = solution.myAtoi(s)
    print(result)
    assert result == -2147483648
