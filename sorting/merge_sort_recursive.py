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
    
    idea:
        divide the array in two partitions recursively, when
        you can't divide further merge them in an ordered version.
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
    left_index, right_index = 0, 0
    
    # ausiliary vector required, increase spatial complexity
    result = []
    
    # compare elements from both vectors and append the lesser
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # add vector's reminders if needed
    result += left[left_index:]
    result += right[right_index:]
    return result

if __name__ == '__main__':
    
    a = [2,4,12,18,5,7,9,15,12]
    b = merge_sort_rec(a)
    print b
