import heapq

def heapsort(collection):
    
    """
    Pure pyton implementation of the heap sort algorithm
    using the heapq native module
    @collection: some mutable collection of unordered items
    @returns: same collection in ascending order
    
    time complexity:
        - lower bound   omega(n log(n))
        - average       theta(n log(n))
        - upper bound   bigO(n log(n))
    
    space complexity:
        - O(1) => in place
    """

    lsorted = []
    heapq.heapify(collection)
    
    while collection:
        smallest = heapq.heappop(collection)
        lsorted.append(smallest)

    return lsorted


if __name__ == '__main__':
    
    a = [2,4,12,18,5,7,9,15,12]
    b = heapsort(a)
    print b
