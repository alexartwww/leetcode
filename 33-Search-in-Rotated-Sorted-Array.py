# Условие задачи (на русском):
# Дан массив, который был отсортирован по возрастанию, а затем "развернут" (rotated)
# в какой-то точке. Все значения в массиве уникальны.
# Нужно найти индекс числа 'target'. Если его нет — вернуть -1.
# Время работы должно быть строго O(log n).
#
# Пример: [0,1,2,4,5,6,7] -> поворот на 3 позиции -> [4,5,6,7,0,1,2]
# Ищем target = 0. Ответ: индекс 4.
#
# -----------------------------------------------------------------------------
# Алгоритм решения: Модифицированный бинарный поиск
#
# Идея: В любом месте, где бы мы ни разделили такой массив пополам,
# ОДНА ИЗ ПОЛОВИН всегда будет идеально отсортирована.
#
# 1. Находим середину (mid).
# 2. Определяем, какая часть отсортирована:
#    - Если nums[left] <= nums[mid], то ЛЕВАЯ часть отсортирована.
#    - Иначе ПРАВАЯ часть отсортирована.
#
# 3. Проверяем, находится ли 'target' внутри отсортированной части:
#    - Если в левой (и target там): сужаем поиск до левой (right = mid - 1).
#    - Иначе идем в правую.
#    - (Аналогично для правой стороны).
#
# 4. Если нашли nums[mid] == target, возвращаем индекс.

import time


class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Шаг 1: Проверяем, отсортирована ли левая часть
            if nums[left] <= nums[mid]:
                # Шаг 2: Если target находится в диапазоне левой части
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Шаг 3: Значит, отсортирована правая часть
            else:
                # Шаг 4: Если target находится в диапазоне правой части
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == '__main__':
    solution = Solution()

    start = time.time()
    result = solution.search([4, 5, 6, 7, 0, 1, 2], 0)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 4
    #
    start = time.time()
    result = solution.search([4, 5, 6, 7, 0, 1, 2], 3)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == -1
    #
    start = time.time()
    result = solution.search([1], 0)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == -1
    #
    start = time.time()
    result = solution.search([4, 5, 6, 7, 0, 1, 2], 4)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 0
    #
    start = time.time()
    result = solution.search([4, 5, 6, 7, 8, 1, 3], 0)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == -1
    #
    start = time.time()
    result = solution.search([3, 4, 5, 6, 1, 2], 2)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 5
    #
    start = time.time()
    result = solution.search([2, 3, 5, 6, 8, 9, 0], 1)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == -1
