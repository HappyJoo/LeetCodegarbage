# 240_Search_a_2D_Matrix at leetcode.com 
# By happyjoo (I love Queen, should I change my name to Freddie? hahahaha)
# I change the minus symbol to underscore. Looks better~
# I was testing if I remember the 74 I did yesterday and then I found out this is the 240:)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        """It's easy to understand. Imaging the matrix.
        We start from the down left number. Let's call it Venom.
        If target is smaller than Venom, we can make sure target is not at the same row of Venom.
        Because they are all bigger than Venom. Such, Others < Venom < target.

        When we get rid of the last row, Venom changes his position to the last second row left one.
        Now we assume target is bigger than Venom, but Venom's still not target yet.
        What now? Is Venom bigger then all of the numbers in the same column up there?
        Aha! We can get rid of those too~

        That's it, we get rid of every row in the bottom and every column in the left until we find the target.
        If still not, we can return False.

        """
        # This is faster than "if not len(matrix) or not len(matrix[0])"
        # I guess it's because it execute less.
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0

        while i >= 0 and j < n:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                i -= 1
            else:
                j += 1
        return False


        # Solution 2 is the same principle as solution 1
        # I just ask Venom go to up right and run toward down left.
        if len(matrix) == 0 or len(matrix[0]) == 0:
                    return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False