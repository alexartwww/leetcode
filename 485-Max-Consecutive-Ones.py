# leetcode: https://leetcode.com/problems/max-consecutive-ones/

# Эта задача — отличная разминка перед более сложными алгоритмами на массивы. Она учит нас работать со счетчиками
# и обновлять глобальный максимум в процессе прохода.

# Условие задачи (на русском):
# Дан массив 'nums', состоящий только из 0 и 1.
# Нужно найти МАКСИМАЛЬНОЕ количество идущих подряд единиц.
#
# Пример 1: nums = [1, 1, 0, 1, 1, 1]
# - Первые две единицы (длина 2)
# - Встретили 0 (счетчик сбросился)
# - Последние три единицы (длина 3)
# Результат: 3
#
# -----------------------------------------------------------------------------
# Алгоритм решения: Линейный проход со счетчиком
#
# Идея: Мы заводим два счетчика:
# 1. current_streak — сколько единиц мы видим прямо сейчас подряд.
# 2. max_streak — самое большое число, которое мы когда-либо видели в current_streak.
#
# 1. Инициализация:
#    current_streak = 0
#    max_streak = 0
#
# 2. Проход по массиву:
#    - Если видим 1: увеличиваем current_streak на 1.
#    - Сразу обновляем max_streak, если текущий счетчик стал больше.
#    - Если видим 0: обнуляем current_streak, так как последовательность прервалась.
#
# 3. Результат:
#    Возвращаем max_streak.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_streak = 0
        current_streak = 0

        for n in nums:
            if n == 1:
                current_streak += 1
                # Обновляем максимум на каждом шаге, где есть единица
                if current_streak > max_streak:
                    max_streak = current_streak
            else:
                # Если встретили 0, цепочка прервалась
                current_streak = 0

        return max_streak


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 1, 0, 1, 1, 1]
    result = solution.findMaxConsecutiveOnes(nums)
    print(result)
    assert result == 3

    nums = [1, 0, 1, 1, 0, 1]
    result = solution.findMaxConsecutiveOnes(nums)
    print(result)
    assert result == 2
