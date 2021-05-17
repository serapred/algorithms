"""
Given an m x n matrix, return true if the matrix is Toeplitz.
Otherwise, return false. A matrix is Toeplitz if every diagonal
from top-left to bottom-right has the same elements.

Note: Remember that lists of lists are not the same as matrices
(as for numpy). Being a list of lists, performing subsetting results
highly inefficient.

To parallelize or simply stream to memory the matrix,
the best approach is to split the matrix in chunks,
by converting the list into an np.array object

sample input:

- matrix = [[1,2,3,4],
            [5,1,2,3],
            [9,5,1,2]]

- matrix = [[1,2],
            [2,2]]

sample output:

- true

- false
"""


def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """

    # notes:
    # 1. a sub-matrix of a Toeplitz matrix
    #    is still a Toeplitz matrix
    # 2. the nth row of a Toeplitz matrix
    #    differs from the nth-1 row by a value
    #    and a right shift
    # 3. a custom more efficient shift can be implemented
    #    since there is no need to prepend the removed tail

    # one liner, based on .2 & .3
    return all(row2[1:] == row1[:-1] for row1, row2 in zip(matrix, matrix[1:]))
