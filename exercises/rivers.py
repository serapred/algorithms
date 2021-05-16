"""
You are given a two-dimensional array (a matrix) of potentially unequal height and width
containing only 0 and 1s.
Each 0 represents land, and each 1 represent part of a river. A river consists of any
number of 1s that are 4-connected (horizontal, vertical adjacency). The number of adjacent
1s determines its size. Note that rivers can twist. In other words it does not have to be
formed by exclusively horizontal or vertical lines (i.e. can be L shaped).

Write a function that returns (in no particular order) an array containin the size of all the rivers represented in the input matrix.

sample input:

- matrix = [[1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0]]

sample output:

- result = [1, 2, 2, 2, 5] # in any order

"""


def neighbours(matrix, pos):

    y, x = pos
    result = []
    if x >= 1:
        result.append((y, x - 1))
    if x < len(matrix[y]) - 1:
        result.append((y, x + 1))
    if y >= 1:
        result.append((y - 1, x))
    if y < len(matrix) - 1:
        result.append((y + 1, x))

    return result


def riverSizes(matrix):

    seen = set()
    result = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] and (i, j) not in seen:

                stack = [(i, j)]
                seen.add((i, j))
                size = 1

                while stack:
                    current = stack.pop()
                    for n in neighbours(matrix, current):
                        y, x = n
                        if matrix[y][x] and n not in seen:
                            seen.add(n)
                            stack.append(n)
                            size += 1

                result.append(size)

    return result
