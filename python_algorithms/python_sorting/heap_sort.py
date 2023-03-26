# Heap Sort has an average-case time complexity of O(n log n), which makes it a very efficient sorting algorithm. 
# However, it has a higher space complexity 
# compared to other sorting algorithms, 
# as it requires an additional heap data structure to store the elements of the array.


def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def heapify(arr, n, i): # this makes max heap
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    heap_sort(arr)
    print("RESULT:", arr)
