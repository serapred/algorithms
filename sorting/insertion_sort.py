def insertion_sort(collection):
    """
    Pure pyton implementation of the insertion sort algorithm
    @collection: some mutable collection of unordered items
    @returns: same collection in ascending order

    time complexity:
        - lower bound   omega(n)
        - average       theta(n^2)
        - upper bound   bigO(n^2)

    space complexity:
        - O(1) => in place
    """

    for i in range(1, len(collection)):
        # switch "<" with ">" to get descending order
        while i > 0 and collection[i] < collection[i - 1]:
            # swap current and previous element
            collection[i], collection[i - 1] = collection[i - 1], collection[i]
            i -= 1  # decrement counter
    return collection


if __name__ == '__main__':

    a = [2, 4, 12, 18, 5, 7, 9, 15, 12]
    b = insertion_sort(a)
    print(b)
