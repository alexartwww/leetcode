# leetcode: https://leetcode.com/problems/cinema-seat-allocation/

# Кинотеатр имеет n рядов сидений, пронумерованных от 1 до n, и в каждом ряду по десять мест, обозначенных
# от 1 до 10, как показано на рисунке выше.

# Дано массив reservedSeats, содержащий количество уже зарезервированных мест. Например, reservedSeats[i] = [3,8]
# означает, что место в 3-м ряду, обозначенное цифрой 8, уже зарезервировано.

# Возвращает максимальное количество групп из четырех человек, которые можно разместить на местах в кинотеатре.
# Группа из четырех человек занимает четыре смежных места в одном ряду. Места через проход (например, [3,3] и [3,4])
# не считаются смежными, но существует исключительный случай, когда проход разделяет группу из четырех человек,
# в этом случае проход разделяет группу из четырех человек посередине, то есть по два человека с каждой стороны.

# Условие задачи (на русском):
# В кинотеатре n рядов по 10 мест. Нужно рассадить группы по 4 человека.
# Места в группе должны быть соседними, но проход (между 3-4 и 7-8)
# может разделять группу только посередине (2+2).
# Это значит, группы могут сидеть на местах: [2,3,4,5], [6,7,8,9] или [4,5,6,7].
#
# -----------------------------------------------------------------------------
# Алгоритм решения: Хеширование и жадная проверка
#
# 1. Собираем занятые места в словарь: {номер_ряда: {множество_занятых_мест}}.
# 2. Для каждого ряда из словаря:
#    - Проверяем возможность посадки в три зоны (лево, право, центр).
#    - Если лево и право свободны -> +2 группы.
#    - Иначе если хотя бы одна из трех зон свободна -> +1 группа.
# 3. Все ряды, которых нет в словаре, дают по 2 группы автоматически.
#
# -----------------------------------------------------------------------------

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        seats = []
        for i in range(n):
            for j in range(10):
                reserved = False
                if j == 0 or j == 9:
                    reserved = True
                else:
                    for k in range(len(reservedSeats)):
                        if reservedSeats[k][0] - 1 == i and reservedSeats[k][1] - 1 == j:
                            reserved = True
                            break
                seats.append(reserved)
        # for i in range(len(seats)):
        #     print(seats[i], end=" ")
        #     if (i+1) % 10 == 0:
        #         print(end="\n")
        result = 0
        i = 0
        while i < len(seats) - 4:
            if ((i + 1) % 2 == 0 or (i + 1) % 4 == 0 or (i + 1) % 6 == 0) and not seats[i] and not seats[i + 1] and not \
            seats[i + 2] and not seats[i + 3]:
                result += 1
                i += 4
            else:
                i += 1
        return result


class Solution2(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}
        for reserved in reservedSeats:
            if reserved[0] in rows:
                rows[reserved[0]] |= 1 << reserved[1]
            else:
                rows[reserved[0]] = 1 << reserved[1]

        # for i in range(1, n+1):
        #     row = rows[i] if i in rows else 0
        #     binary = "{:b}".format(row)
        #     print(binary.rjust(11, '0')[::-1][1:])
        result = 0
        search = [1 << 2 | 1 << 3 | 1 << 4 | 1 << 5, 1 << 4 | 1 << 5 | 1 << 6 | 1 << 7, 1 << 6 | 1 << 7 | 1 << 8 | 1 << 9]
        result += (n - len(rows)) * 2
        for row in rows.values():
            for s in search:
                if row & s == 0:
                    row |= s
                    result += 1
        return result


if __name__ == '__main__':
    solution = Solution2()

    n = 3
    reservedSeats = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
    result = solution.maxNumberOfFamilies(n, reservedSeats)
    print(result)
    assert result == 4

    n = 2
    reservedSeats = [[2, 1], [1, 8], [2, 6]]
    result = solution.maxNumberOfFamilies(n, reservedSeats)
    print(result)
    assert result == 2

    n = 4
    reservedSeats = [[4, 3], [1, 4], [4, 6], [1, 7]]
    result = solution.maxNumberOfFamilies(n, reservedSeats)
    print(result)
    assert result == 4

    n = 4
    reservedSeats = [[2, 10], [3, 1], [1, 2], [2, 2], [3, 5], [4, 1], [4, 9], [2, 7]]
    result = solution.maxNumberOfFamilies(n, reservedSeats)
    print(result)
    assert result == 3
