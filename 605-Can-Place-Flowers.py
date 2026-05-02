# leetcode: https://leetcode.com/problems/can-place-flowers/

# Эта задача на Greedy (Жадный алгоритм). Основная идея проста: мы идем по грядке слева направо и сажаем цветок
# в каждое доступное место, как только его находим. Если в конце мы смогли посадить хотя бы n цветов, значит,
# ответ — true.

# Условие задачи (на русском):
# Дана грядка (массив из 0 и 1) и число 'n'.
# 1 — цветок уже растет, 0 — пусто.
# Цветы нельзя сажать рядом (соседние ячейки не могут быть обе равны 1).
# Нужно проверить, можно ли посадить 'n' новых цветов.
#
# Пример 1: flowerbed = [1, 0, 0, 0, 1], n = 1
# Мы можем посадить цветок в центр: [1, 0, 1, 0, 1].
# Результат: true
#
# -----------------------------------------------------------------------------
# Алгоритм решения: Жадный проход (Greedy)
#
# Идея: Проходим по массиву и проверяем каждую ячейку.
# Мы можем посадить цветок в ячейку 'i', если:
# 1. Сама ячейка пуста: flowerbed[i] == 0
# 2. Левый сосед пуст (или это начало грядки): i == 0 or flowerbed[i-1] == 0
# 3. Правый сосед пуст (или это конец грядки): i == len-1 or flowerbed[i+1] == 0
#
# Как только посадили цветок, уменьшаем 'n' и помечаем ячейку как 1.
# Если 'n' стало <= 0, можно сразу возвращать true.
#
# 1. Проход по массиву:
#    - Проверка условий (лево, право, текущая).
#    - Посадка (n -= 1, flowerbed[i] = 1).
# 2. Итог: n <= 0.

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        # Если цветов нужно 0, то всегда true
        if n <= 0:
            return True

        length = len(flowerbed)

        for i in range(length):
            # Проверяем, пуста ли текущая ячейка
            if flowerbed[i] == 0:
                # Проверяем левого соседа
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                # Проверяем правого соседа
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    # Сажаем цветок
                    flowerbed[i] = 1
                    n -= 1

                    # Если уже посадили всё, что нужно — выходим
                    if n <= 0:
                        return True

        return n <= 0


if __name__ == '__main__':
    solution = Solution()

    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    result = solution.canPlaceFlowers(flowerbed, n)
    print(result)
    assert result == True

    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    result = solution.canPlaceFlowers(flowerbed, n)
    print(result)
    assert result == False
