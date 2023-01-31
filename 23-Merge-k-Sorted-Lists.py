import time
from . import ListNode


class Solution1:
    def mergeKLists(self, lists):
        result = None
        current_result = None
        while True:
            min_i = None
            for i, l in enumerate(lists):
                if l is None:
                    continue
                if min_i is None or (min_i is not None and l.val <= lists[min_i].val):
                    min_i = i

            if min_i is None:
                break
            if result is None:
                result = ListNode(lists[min_i].val)
                current_result = result
            else:
                current_result.next = ListNode(lists[min_i].val)
                current_result = current_result.next
            if lists[min_i].next is not None:
                lists[min_i] = lists[min_i].next
            else:
                del lists[min_i]

        return result

class Solution2:
    def merge2Lists(self, list1, list2):
        result = None
        if result is None:
            if list1.val <= list2.val:
                result = list1
                list1 = list1.next
            else:
                result = list2
                list2 = list2.next
        if list1 is None:
            result.next = list2
            return result
        elif list2 is None:
            result.next = list1
            return result
        cursor = result
        while True:
            if list1.val <= list2.val:
                cursor.next = list1
                list1 = list1.next
            else:
                cursor.next = list2
                list2 = list2.next
            cursor = cursor.next
            if list1 is None:
                cursor.next = list2
                break
            elif list2 is None:
                cursor.next = list1
                break
        return result

    def mergeKLists(self, lists):
        if lists is None or len(lists) == 0:
            return None
        result = None
        for i, l in enumerate(lists):
            if result is None:
                result = l
                continue
            if l is not None:
                result = self.merge2Lists(result, l)
        return result


if __name__ == '__main__':
    # [[1, 4, 5], [1, 3, 4], [2, 6]]
    solution = Solution2()
    start = time.time()
    lists = [ListNode(1).append_to_tail(4).append_to_tail(5),
         ListNode(1).append_to_tail(3).append_to_tail(4),
         ListNode(2).append_to_tail(6)]
    result = solution.mergeKLists(lists)
    print(result, '{:.4f}'.format(time.time() - start))
