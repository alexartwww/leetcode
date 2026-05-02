# Условие задачи (на русском):
# Дана строка 's' и число 'k'. Нужно найти подстроку длиной ровно 'k',
# в которой содержится максимальное количество гласных букв.
# Гласными считаются: 'a', 'e', 'i', 'o', 'u'.
#
# Пример 1: s = "abciiidef", k = 3
# - Окно "abc" -> 1 гласная ('a')
# - Окно "bci" -> 1 гласная ('i')
# - Окно "iii" -> 3 гласные ('i', 'i', 'i')
# Результат: 3
#
# -----------------------------------------------------------------------------
# Алгоритм решения: Скользящее окно фиксированного размера
#
# Идея: Мы поддерживаем "окно" длиной 'k'. Когда окно сдвигается вправо:
# 1. Мы добавляем один новый символ (справа).
# 2. Мы выбрасываем один старый символ (слева).
# 3. Нам не нужно пересчитывать все гласные внутри заново, достаточно проверить
#    только эти два символа (вошедший и вышедший).
#
# 1. Инициализация:
#    - Определяем множество гласных vowels = {'a', 'e', 'i', 'o', 'u'} для быстрого поиска.
#    - Считаем количество гласных в самом первом окне (от 0 до k-1).
#    - Запоминаем это число как текущее (current_vowels) и максимальное (max_vowels).
#
# 2. Скольжение:
#    - Идем циклом от k до конца строки.
#    - Если вошедший символ s[i] — гласный: current_vowels += 1.
#    - Если вышедший символ s[i - k] — гласный: current_vowels -= 1.
#    - Обновляем max_vowels на каждом шаге.
#
# 3. Оптимизация:
#    - Если в какой-то момент max_vowels стало равно k, можно сразу возвращать k,
#      так как больше гласных в окне длиной k быть не может.

class Solution(object):
    def maxVowels(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}

        current_vowels = 0
        # 1. Считаем гласные в первом окне
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        # 2. Двигаем окно
        for i in range(k, len(s)):
            # Если нашли максимум, выходим раньше
            if max_vowels == k:
                return k

            # Добавляем правый элемент
            if s[i] in vowels:
                current_vowels += 1
            # Убираем левый элемент (который теперь за пределами окна)
            if s[i - k] in vowels:
                current_vowels -= 1

            if current_vowels > max_vowels:
                max_vowels = current_vowels

        return max_vowels



if __name__ == '__main__':
    solution = Solution()

    s = "abciiidef"
    k = 3
    result = solution.maxVowels(s, k)
    print(result)
    assert result == 3

    s = "aeiou"
    k = 2
    result = solution.maxVowels(s, k)
    print(result)
    assert result == 2

    s = "leetcode"
    k = 3
    result = solution.maxVowels(s, k)
    print(result)
    assert result == 2
