import time


class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0 or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        row = 0
        left = 0
        right = len(matrix) - 1

        while True:
            if left >= right:
                row = left
                break
            if left > 0 and target > matrix[left - 1][-1] and target < matrix[left][0]:
                return False
            if right < len(matrix) - 1 and target > matrix[right - 1][-1] and target < matrix[right][0]:
                return False
            if target > matrix[left][-1]:
                left = left + 1
            if target < matrix[right][0]:
                right = right - 1

        if len(matrix[row]) == 0:
            return False

        column = 0
        left = 0
        right = len(matrix[row]) - 1

        while True:
            if target == matrix[row][left] or target == matrix[row][right]:
                return True
            if left >= right:
                break
            if target > matrix[row][left]:
                left = left + 1
            if target < matrix[row][right]:
                right = right - 1

        return False


if __name__ == '__main__':
    solution = Solution()

    #
    start = time.time()
    result = solution.searchMatrix(
        [[-9, -9, -9, -7, -5, -3, -3, -3], [-2, -2, 0, 1, 2, 3, 3, 4], [5, 5, 5, 7, 9, 11, 11, 12],
         [14, 14, 15, 16, 18, 18, 19, 20], [21, 23, 24, 25, 27, 29, 30, 31], [34, 35, 37, 38, 38, 38, 40, 40],
         [42, 44, 44, 45, 47, 47, 47, 48], [50, 51, 51, 52, 53, 54, 56, 56], [58, 59, 60, 62, 64, 64, 64, 66]], 5)
    print(result, '{}'.format(time.time() - start))
    assert result == True

    #
    start = time.time()
    result = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
    print(result, '{}'.format(time.time() - start))
    assert result == False
    #
    start = time.time()
    result = solution.searchMatrix(
        [[-8, -7, -5, -3, -3, -1, 1], [2, 2, 2, 3, 3, 5, 7], [8, 9, 11, 11, 13, 15, 17], [18, 18, 18, 20, 20, 20, 21],
         [23, 24, 26, 26, 26, 27, 27], [28, 29, 29, 30, 32, 32, 34]], -5)
    print(result, '{}'.format(time.time() - start))
    assert result == True
    #
    start = time.time()
    result = solution.searchMatrix([[1], [3]], 0)
    print(result, '{}'.format(time.time() - start))
    assert result == False
    #
    start = time.time()
    result = solution.searchMatrix(
        [[-8, -6, -5, -4, -2, -1, -1, 0, 2, 4, 5, 7, 7, 7, 7, 9, 9, 9, 9, 11],
         [12, 14, 15, 16, 18, 20, 20, 20, 21, 21, 22, 23, 23, 25, 25, 25, 26, 27, 29, 30],
         [31, 31, 32, 32, 33, 35, 37, 39, 39, 39, 40, 41, 43, 44, 46, 48, 48, 48, 48, 50],
         [52, 54, 55, 57, 57, 58, 58, 60, 62, 64, 65, 65, 65, 67, 69, 71, 71, 73, 74, 74],
         [75, 76, 78, 78, 80, 82, 82, 82, 84, 85, 85, 87, 87, 89, 90, 90, 91, 93, 93, 94],
         [96, 98, 100, 102, 104, 105, 107, 109, 111, 113, 113, 115, 115, 117, 119, 119, 120, 122, 122, 124],
         [126, 127, 128, 130, 130, 130, 130, 132, 132, 133, 134, 136, 137, 138, 140, 141, 141, 143, 144, 146],
         [148, 150, 151, 152, 154, 156, 157, 158, 159, 161, 161, 162, 162, 164, 164, 165, 167, 168, 169, 169],
         [171, 173, 173, 175, 176, 178, 179, 181, 182, 183, 184, 184, 184, 185, 186, 186, 186, 186, 187, 189],
         [190, 192, 192, 193, 195, 196, 197, 197, 198, 198, 198, 198, 198, 199, 201, 203, 204, 206, 208, 208],
         [209, 210, 211, 212, 212, 212, 214, 214, 216, 217, 218, 218, 219, 221, 222, 224, 225, 227, 229, 229],
         [230, 230, 230, 231, 233, 233, 234, 235, 237, 237, 238, 238, 240, 240, 242, 242, 244, 246, 246, 247],
         [249, 251, 252, 252, 254, 254, 256, 256, 257, 258, 259, 260, 260, 261, 263, 265, 266, 267, 267, 269],
         [271, 273, 273, 274, 274, 274, 276, 276, 276, 278, 279, 280, 280, 280, 282, 284, 284, 286, 286, 287],
         [289, 290, 290, 291, 293, 293, 293, 293, 295, 296, 296, 297, 298, 299, 299, 301, 302, 304, 306, 308],
         [309, 310, 311, 311, 312, 312, 314, 315, 317, 319, 320, 322, 323, 324, 324, 324, 326, 328, 329, 331],
         [332, 334, 335, 337, 337, 339, 341, 343, 345, 347, 348, 348, 348, 348, 348, 350, 350, 350, 351, 352],
         [353, 355, 355, 356, 357, 358, 360, 361, 361, 361, 362, 364, 364, 364, 365, 366, 368, 370, 370, 372],
         [374, 376, 378, 380, 382, 382, 383, 384, 385, 385, 387, 388, 388, 390, 392, 394, 394, 396, 397, 399],
         [400, 402, 403, 403, 405, 405, 407, 409, 411, 411, 413, 414, 415, 417, 418, 419, 419, 419, 421, 422]], 271)
    print(result, '{}'.format(time.time() - start))
    assert result == True
    #
    start = time.time()
    result = solution.searchMatrix(
        [[-8, -8, -7, -7, -6, -5, -3, -2], [0, 0, 1, 3, 4, 6, 8, 8], [11, 12, 14, 16, 18, 18, 19, 19],
         [22, 23, 25, 27, 28, 30, 30, 31], [34, 35, 37, 39, 40, 42, 43, 45], [48, 50, 51, 51, 53, 54, 55, 57],
         [58, 60, 62, 62, 62, 63, 63, 65], [68, 69, 71, 72, 72, 72, 74, 76]], 76)
    print(result, '{}'.format(time.time() - start))
    assert result == True
    #
    start = time.time()
    result = solution.searchMatrix([[1], [3]], 2)
    print(result, '{}'.format(time.time() - start))
    assert result == False
    #
    start = time.time()
    result = solution.searchMatrix([[1], [3]], 0)
    print(result, '{}'.format(time.time() - start))
    assert result == False
    #
    start = time.time()
    result = solution.searchMatrix([[1, 3]], 1)
    print(result, '{}'.format(time.time() - start))
    assert result == True
    #
    start = time.time()
    result = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 30)
    print(result, '{}'.format(time.time() - start))
    assert result == True
    #
    start = time.time()
    result = solution.searchMatrix([[1]], 0)
    print(result, '{}'.format(time.time() - start))
    assert result == False
