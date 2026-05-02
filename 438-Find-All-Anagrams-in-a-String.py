# Алгоритм решения: Скользящее окно фиксированного размера + Словари частот
#
# Суть: Анаграмма — это слово, в котором те же буквы в том же количестве.
# Значит, нам нужно найти в строке 's' все окна длиной как 'p',
# состав которых (частота букв) полностью совпадает с составом 'p'.
#
# 1. Инициализация:
#    - Создаем два словаря (или массива на 26 элементов) для подсчета букв:
#      p_count (эталон из строки p) и s_count (текущее окно в s).
#    - Наполняем p_count и самое первое окно s_count (длиной len(p)).
#
# 2. Первое сравнение:
#    - Если p_count == s_count, значит первое окно — анаграмма. Добавляем индекс 0.
#
# 3. Скольжение окна (от len(p) до конца s):
#    - Добавляем в s_count новый символ (справа).
#    - Удаляем из s_count старый символ (тот, что остался слева).
#      Важно: если счетчик символа стал 0, удаляем ключ из словаря, чтобы
#      сравнение словарей p_count == s_count работало корректно.
#    - Если после сдвига словари равны — добавляем индекс начала окна в результат.
#
# Пример: s = "cbaebabacd", p = "abc"
#
# - p_count = {'a':1, 'b':1, 'c':1}. Длина окна = 3.
# - Окно 1: "cba". s_count = {'c':1, 'b':1, 'a':1}. Равны! Индекс 0 в результат.
# - Сдвиг: Добавляем 'e', убираем 'c'. Окно "bae". Не равно p_count.
# - Сдвиг: Добавляем 'b', убираем 'b'. Окно "aeb". Не равно.
# ...
# - Доходим до окна "bac": s_count снова {'b':1, 'a':1, 'c':1}. Равны! Индекс 6.

import time
from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s): return []

        p_count, s_count = {}, {}
        # Заполняем словари для первого окна
        for i in range(len(p)):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        res = [0] if p_count == s_count else []

        left = 0
        # Начинаем двигать окно
        for right in range(len(p), len(s)):
            # Добавляем символ справа
            s_count[s[right]] = s_count.get(s[right], 0) + 1
            # Убираем символ слева
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]

            left += 1

            # Сравниваем состав текущего окна с эталоном
            if s_count == p_count:
                res.append(left)

        return res


if __name__ == '__main__':
    solution = Solution()

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
