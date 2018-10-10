import heapq

def heapsort(collection):
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
