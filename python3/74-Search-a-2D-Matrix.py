class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Solution 1
        # This is the easiest way, beat 27.93% at 2019.3.27
        # Just iterate all of the numbers in every list[list]
        if not matrix: #If matrix is [] then it should return False
        # BTW, if it's "if len(matrix) == 0:" will only beat 2.68%
        # I guess it's beacuse it has to execute twice. Fst, len(matrix) Snd, compare to 0
            return False
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True

        
        # Solution 2 and 3 are both bisection, almost the same
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        low, high = 0, row * col - 1

        while low <= high: # when low > high, the list run out
            mid = (low + high) // 2
            # a[x] = matrix[x / m][x % m]
            mid_elem = matrix[mid // col][mid % col] # // in python3 means not decimal
            if mid_elem == target:
                return True
            elif mid_elem < target:
                low = mid + 1
            else:
                high = mid - 1
        return False # The list run out and should return a False 


        # Solution 3
        # from functools import reduce (No need to explain how to import, right?)
        if not matrix:
            return False
        # reduce((lambda x, y: x * y), [1, 2, 3, 4]) == 1*2*3*4
        # It applies a rolling computation to sequential pairs of values in a list.
        new_matrix = reduce(lambda x, y: x + y, matrix) # Turn the matrix to normal list.
        low, high = 0, len(new_matrix)-1
        while low <= high:
            mid = (low + high) // 2
            if new_matrix[mid] == target:
                return True
            elif new_matrix[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
