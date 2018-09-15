def bubble_sort(collection):

    """
    Pure pyton implementation of the bubble sort algorithm
    @collection: some mutable collection of unordered items
    @returns: same collection in ascending order
    
    time complexity:
        - lower bound   omega(n)
        - average       theta(n^2)
        - upper bound   bigO(n^2)
    
    space complexity:
        - O(1) => in place
    """

    swap = True # flags to determine if at any scan a swap op has taken place
    length = len(collection)
    
    while swap:
        swap = False
        for i in range(0,length-1):
            if collection[i] > collection[i+1]:
                collection[i], collection[i+1] = collection[i+1], collection[i]
                swap = True
        
        # decrementing the length on the assumption that
        # at each iteration the n-ith element will be 
        # in its final position
        length -= 1

    return collection


if __name__ == '__main__':
    
    c = [3,2,4,1,5]
    print bubble_sort(c)
