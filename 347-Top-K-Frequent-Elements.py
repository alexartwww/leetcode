# Условие задачи (на русском):
# Дан массив чисел 'nums' и число 'k'.
# Нужно вернуть 'k' самых часто встречающихся элементов.
# Порядок в ответе не важен.
#
# Пример: nums = [1,1,1,2,2,3], k = 2
# 1 встречается 3 раза, 2 встречается 2 раза, 3 встречается 1 раз.
# Ответ: [1, 2]
#
# -----------------------------------------------------------------------------
# Алгоритм решения: Блочная сортировка (Bucket Sort) за O(n)
#
# 1. Считаем частоты: {число: количество}.
# 2. Создаем "корзины": индекс массива — это частота появления.
#    Максимальная частота не может быть больше длины массива nums.
# 3. Собираем результат, двигаясь от конца массива корзин к началу.
#
# -----------------------------------------------------------------------------

import heapq
import time
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        result = [0 for _ in range(k)]
        for i in range(k):
            max = 0
            for key in d:
                if d[key] > max:
                    max = d[key]
                    result[i] = key
            del d[result[i]]

        return result


class Solution2:
    def topKFrequent(self, nums, k):
        counts = Counter(nums)
        heap = []
        for key, count in counts.items():
            heapq.heappush(heap, [-count, key])

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


class Solution3:
    def topKFrequent(self, nums, k):
        if len(nums) == 0 or len(nums) == 1:
            return nums
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        d2 = {}
        for num in d:
            freq = d[num]
            if freq not in d2:
                d2[freq] = [num]
            else:
                d2[freq].append(num)

        result = []
        for freq in sorted(d2.keys(), reverse=True):
            for num in d2[freq]:
                result.append(num)
                if len(result) == k:
                    return result


if __name__ == '__main__':
    solution = Solution3()

    start = time.time()
    result = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [1, 2]

    start = time.time()
    result = solution.topKFrequent([1], 1)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [1]

    start = time.time()
    result = solution.topKFrequent([1,1,1,2,2,3], 2)
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [1,2]
