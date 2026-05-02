# Это классическая задача на Linked Lists (Связные списки). Она имитирует сложение чисел "в столбик",
# которое мы учили в школе, но с одним приятным бонусом: числа уже записаны в обратном порядке.
# Это значит, что единицы стоят в самом начале списка, потом десятки, сотни и так далее — как раз так,
# как нам удобно для сложения.

# Условие задачи (на русском):
# Даны два связных списка, представляющих два неотрицательных целых числа.
# Цифры хранятся в обратном порядке (единицы в начале).
# Нужно сложить эти числа и вернуть результат в виде нового связного списка.
#
# Пример 1: l1 = [2,4,3], l2 = [5,6,4]
# Это числа 342 и 465.
# 2+5 = 7
# 4+6 = 10 (пишем 0, 1 в уме)
# 3+4+1(из ума) = 8
# Результат: [7,0,8] (число 807)
#
# -----------------------------------------------------------------------------
# Алгоритм решения: Имитация сложения в столбик
#
# Идея: Мы идем по обоим спискам одновременно, складываем цифры и
# переносим "десяток" (carry) на следующий шаг.
#
# 1. Инициализация:
#    - dummy = ListNode(0) — "пустышка", чтобы было удобно цеплять результат.
#    - curr = dummy — указатель на текущий узел нового списка.
#    - carry = 0 — переменная для хранения переноса (0 или 1).
#
# 2. Основной цикл:
#    Работает, пока есть узлы в l1 ИЛИ в l2 ИЛИ остался carry.
#    - Берем значения из узлов (если список закончился, берем 0).
#    - Считаем сумму: val1 + val2 + carry.
#    - Обновляем carry: сумма // 10.
#    - Создаем новый узел с цифрой: сумма % 10.
#    - Двигаем указатели l1, l2 и curr вперед.
#
# 3. Результат:
#    - Возвращаем dummy.next (так как первый узел был техническим нулем).


# Определение узла односвязного списка, которое использует LeetCode:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Число, которое хранится в узле
        self.next = next  # Ссылка на следующий узел (или None, если это конец)


def array_to_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next


def list_to_array(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


class Solution:
    def addTwoNumbers(self, l1, l2):
        # Создаем фиктивную голову списка для удобства
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # Работаем, пока не пройдем оба списка и пока нет остатка в уме
        while l1 or l2 or carry:
            # Получаем значения из текущих узлов, если они есть
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Считаем сумму и новый перенос
            total = val1 + val2 + carry
            carry = total // 10
            val = total % 10

            # Создаем новый узел в результирующем списке
            curr.next = ListNode(val)

            # Двигаем указатели
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


if __name__ == '__main__':
    # Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
    # Output: [7, 0, 8]
    # Explanation: 342 + 465 = 807.

    solution = Solution()

    l1 = array_to_list([2, 4, 3])
    l2 = array_to_list([5, 6, 4])
    result = list_to_array(solution.addTwoNumbers(l1, l2))
    print(result)
    assert result == [7, 0, 8]

    l1 = array_to_list([0])
    l2 = array_to_list([0])
    result = list_to_array(solution.addTwoNumbers(l1, l2))
    print(result)
    assert result == [0]

    l1 = array_to_list([9, 9, 9, 9, 9, 9, 9])
    l2 = array_to_list([9, 9, 9, 9])
    result = list_to_array(solution.addTwoNumbers(l1, l2))
    print(result)
    assert result == [8, 9, 9, 9, 0, 0, 0, 1]
