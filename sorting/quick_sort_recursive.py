def quick_sort_rec(collection):
    
    """
    Pure pyton implementation of the quick sort algorithm (recursive version)
    @collection: some mutable collection of unordered items
    @returns: same collection in ascending order
    
    time complexity:
        - lower bound   omega(n log(n))
        - avarage       theta(n log(n))
        - upper bound   bigO(n^2)
    
    space complexity:
        - O(1) => no ausiliary vector needed
    """

    def quick_sort_helper(collection, start, end):   
        if start < end:
            pivot = partitioning(collection,start,end)
            quick_sort_helper(collection,start,pivot-1)
            quick_sort_helper(collection,pivot+1,end)

    quick_sort_helper(collection,0,len(collection)-1)

    return collection

def partitioning(alist, start, end):
    
    left  = start + 1
    right = end
    pivot = start

    while True:

        # the = guarantees that the index 
        # will eventually cross
        
        # scanning the partition
        # index condition before value condition
        # to avoid possible out of range exceptions

        # left -> right for elements larger than pivot 
        while left <= right and alist[left] <= alist[pivot]:
            left += 1

        # right -> left for elements smaller than pivot
        while right >= left and alist[right] >= alist[pivot]:
            right -= 1
        
        if right < left:
            break # indexes crossed
        else:
            # a swappable couple was found
            alist[left], alist[right] = alist[right],alist[left]

   # taking the pivot as first element means that
   # it has to be swapped with the right pointer
   # since it scans for values smaller than the pivot
    alist[pivot], alist[right] = alist[right], alist[pivot]

    return right



if __name__ == '__main__':
    
    a = [9,24,3,9,12,15,8,7,9,16,6]

    quick_sort_rec(a)

    print a
