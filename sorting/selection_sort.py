def selection_sort(collection):
    """
    Pure pyton implementation of the selection sort algorithm
    @collection: some mutable collection of unordered items
    @returns: same collection in ascending order

    time complexity:
        - lower bound   omega(n^2)
        - average       theta(n^2)
        - upper bound   bigO(n^2)

    space complexity:
        - O(1) => in place
    """

    # since this is called twice it's better to save it
    length = len(collection)

    for i in range(length):
        smallest = i
        for j in range(i + 1, length):
            if collection[j] < collection[smallest]:
                smallest = j
        if smallest != i:
            collection[i], collection[smallest] = collection[smallest], collection[i]

    return collection


if __name__ == '__main__':

    a = [2, 4, 12, 18, 5, 7, 9, 15, 12]
    b = selection_sort(a)
    print(b)
