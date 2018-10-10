def heapsort(collection):

    n = len(collection)

    for i in range(n,-1,-1):
        max_heapify(collection,n,i)

    for i in range(n-1,0,-1):
        collection[0],collection[i] = collection[i],collection[0]
        max_heapify(collection,i,0)

    return collection

def left(root):
    return 2 * root + 1

def right(root):
    return 2 * root + 2

def max_heapify(collection, size, root):
    
    largest = root
    l = left(root)
    r = right(root)

    if l < size and collection[l] > collection[largest]:
        largest = l
    if r < size and collection[r] > collection[largest]:
        largest = r

    if largest != root:
        collection[root], collection[largest] = collection[largest], collection[root]
        max_heapify(collection,size,largest)


if __name__ == '__main__':
    
    a = [2,4,12,18,5,7,9,15,12]
    b = heapsort(a)
    print b
