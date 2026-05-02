# leetcode: https://leetcode.com/problems/merge-intervals/

# Эта задача на Sorting (Сортировку) и Greedy (Жадный алгоритм). Ключ к решению в том, чтобы сначала упорядочить
# интервалы. Как только они отсортированы по времени начала, все потенциально перекрывающиеся
# интервалы окажутся соседями.

# Условие задачи (на русском):
# Дан массив интервалов [start, end]. Нужно объединить все перекрывающиеся
# интервалы в один и вернуть список уникальных непересекающихся интервалов.
#
# Пример: [[1, 3], [2, 6], [8, 10]]
# 1. [1, 3] и [2, 6] пересекаются, так как 2 < 3.
# 2. Объединяем их в [1, 6] (берем начало первого и максимум из концов).
# 3. [1, 6] и [8, 10] не пересекаются, так как 8 > 6.
# Результат: [[1, 6], [8, 10]]
#
# -----------------------------------------------------------------------------
# Алгоритм решения: Сортировка и один проход
#
# 1. Сортировка: Сортируем массив интервалов по их начальному значению (x[0]).
#    Это гарантирует, что если интервал B может начаться раньше конца интервала A,
#    то B будет идти сразу за A.
#
# 2. Слияние:
#    - Создаем список 'merged' и кладем туда первый интервал.
#    - Идем по остальным интервалам:
#      - Если начало текущего интервала <= конца последнего добавленного в 'merged':
#        Значит, они перекрываются. Обновляем конец последнего интервала в 'merged',
#        выбирая максимальный из двух концов.
#      - Иначе:
#        Интервалы не пересекаются. Просто добавляем текущий интервал в 'merged'.
#
# -----------------------------------------------------------------------------

import time


class Solution(object):
    def merge(self, intervals):
        # Сортируем по стартовому времени
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            # Если список пуст или нет пересечения
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Есть пересечение, объединяем с последним добавленным
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == '__main__':
    solution = Solution()

    start = time.time()
    result = solution.merge([[1, 4], [2, 3]])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[1,4]]
    start = time.time()
    result = solution.merge([[1,4],[0,0]])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[0,0],[1,4]]
    start = time.time()
    result = solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[1, 6], [8, 10], [15, 18]]
    start = time.time()
    result = solution.merge([[1, 4], [0, 1]])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[0, 4]]
    start = time.time()
    result = solution.merge([[1, 4], [4, 5]])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[1, 5]]
    start = time.time()
    result = solution.merge([[1, 4], [0, 4]])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == [[0, 4]]
