def merge_sort_rec(collection):
    
    """
    Pure pyton implementation of the merge sort algorithm (recursive version)
    @collection: some mutable collection of unordered items
    @returns: same collection in ascending order
    
    time complexity:
        - lower bound   omega(n log(n))
        - avarage       theta(n log(n))
        - upper bound   bigO(n log(n))
    
    space complexity:
        - O(n) => ausiliary vector needed
    """

    if len(collection) <= 1: #base case
        return collection

    #split collection in half and sort recursively
    middle = len(collection) // 2
    left  = merge_sort_rec(collection[:middle])
    right = merge_sort_rec(collection[middle:])
    return merge(left,right)


def merge(left,right):

    #sliding indexes
    i, j = 0, 0
    
    # ausiliary vector required, increase spatial complexity
    result = []
    
    # compare elements from both vectors and append the lesser
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # add vector's reminders if needed
    result += left[i:]
    result += right[j:]
    return result

if __name__ == '__main__':
    
    a = [2,4,12,18,5,7,9,15,12]
    b = merge_sort_rec(a)
    print b
