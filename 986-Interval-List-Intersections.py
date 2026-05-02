# leetcode: https://leetcode.com/problems/interval-list-intersections/

# Вам даны два списка замкнутых интервалов, firstList и secondList, где firstList[i] = [starti, endi]
# и secondList[j] = [startj, endj]. Каждый список интервалов попарно не пересекается и отсортирован.
#
# Верните пересечение этих двух списков интервалов.
#
# Замкнутый интервал [a, b] (где a <= b) обозначает множество действительных чисел x, для которых a <= x <= b.
#
# Пересечение двух замкнутых интервалов — это множество действительных чисел, которые либо пусты, либо представлены
# в виде замкнутого интервала. Например, пересечение [1, 3] и [2, 4] — это [2, 3].

# Условие задачи (на русском):
# Даны два списка замкнутых интервалов, каждый из которых отсортирован
# и внутри списка интервалы не пересекаются.
# Нужно найти все пересечения между интервалами первого и второго списка.
#
# Пример: [1, 3] и [2, 4] пересекаются в [2, 3].
# Правило пересечения: [max(start1, start2), min(end1, end2)]
# Пересечение существует, только если start_max <= end_min.
#
# -----------------------------------------------------------------------------
# Алгоритм решения: Два указателя
#
# Идея:
# Мы ставим по указателю (i и j) на начало каждого списка.
# На каждом шаге мы проверяем, пересекаются ли текущие интервалы.
#
# 1. Находим потенциальное пересечение:
#    - start = max(firstList[i][0], secondList[j][0])
#    - end = min(firstList[i][1], secondList[j][1])
#
# 2. Если start <= end, добавляем [start, end] в результат.
#
# 3. Как двигать указатели?
#    Мы сдвигаем указатель того интервала, который закончился РАНЬШЕ.
#    Тот, кто закончился позже, может еще пересечься со следующим интервалом
#    из другого списка.
#
# -----------------------------------------------------------------------------

class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        current_i = 0
        current_j = 0
        result = []

        while current_i < len(firstList) and current_j < len(secondList):
            # проверка пересечения
            if firstList[current_i][1] >= secondList[current_j][0] and firstList[current_i][0] <= secondList[current_j][1]:
                interval = [max(firstList[current_i][0], secondList[current_j][0]), min(firstList[current_i][1], secondList[current_j][1])]
                if len(result) == 0:
                    result.append(interval)
                elif result[-1][0] >= interval[0]:
                    result[-1][1] = max(result[-1][1], interval[1])
                else:
                    result.append(interval)
            if firstList[current_i][1] < secondList[current_j][1]:
                current_i += 1
            else:
                current_j += 1


        return result


class Solution2(object):
    def intervalIntersection(self, firstList, secondList):
        i = 0  # Указатель для первого списка
        j = 0  # Указатель для второго списка
        res = []

        while i < len(firstList) and j < len(secondList):
            # Находим границы пересечения
            start_max = max(firstList[i][0], secondList[j][0])
            end_min = min(firstList[i][1], secondList[j][1])

            # Если пересечение существует
            if start_max <= end_min:
                res.append([start_max, end_min])

            # Двигаем указатель того интервала, который заканчивается раньше
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return res


if __name__ == '__main__':
    solution = Solution2()

    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]

    result = solution.intervalIntersection(firstList, secondList)
    print(result)
    assert result == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
