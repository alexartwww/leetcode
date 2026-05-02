# Условие задачи (на русском):
# Дан массив строк 'strs'. Нужно сгруппировать анаграммы вместе.
# Анаграммы — это слова, состоящие из одних и тех же букв в одинаковом количестве.
#
# Пример: strs = ["eat","tea","tan","ate","nat","bat"]
# Результат: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# -----------------------------------------------------------------------------
# Алгоритм решения: Хеширование отсортированной строки
#
# Идея: Если мы отсортируем буквы в словах "eat", "tea" и "ate",
# то все они превратятся в одну и ту же строку — "aet".
# Эта отсортированная строка станет нашим КЛЮЧОМ в словаре.
#
# 1. Создаем пустой словарь (Hash Map), где:
#    - Ключ (Key) = отсортированная строка.
#    - Значение (Value) = список исходных слов-анаграмм.
#
# 2. Проходим по каждой строке 's' из массива:
#    - Сортируем буквы в строке: sorted_s = "".join(sorted(s))
#    - Добавляем исходное слово 's' в словарь по ключу sorted_s.
#
# 3. Возвращаем все значения словаря (списки групп).

import time


class Solution(object):
    def groupAnagrams(self, strs):
        # Используем обычный словарь
        groups = {}

        for s in strs:
            # Получаем ключ (отсортированную строку)
            # sorted() возвращает список ['a', 'e', 't'], join склеивает в 'aet'
            key = "".join(sorted(s))

            # Если такого ключа еще не было, инициализируем список
            if key not in groups:
                groups[key] = []

            # Добавляем оригинальное слово в список этой группы
            groups[key].append(s)

        # Возвращаем список всех списков (групп)
        return list(groups.values())


if __name__ == '__main__':
    solution = Solution()
    start = time.time()
    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    start = time.time()
    result = solution.groupAnagrams([""])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[""]]
    start = time.time()
    result = solution.groupAnagrams(["a"])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [["a"]]
