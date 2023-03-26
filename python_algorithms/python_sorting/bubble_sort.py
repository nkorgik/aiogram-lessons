# In most practical applications, bubble sort is not the preferred choice of sorting algorithm due to its slow runtime complexity, especially for large datasets. 
# As I mentioned earlier, the worst-case and average-case time complexity of bubble sort is O(n^2), 
# which means that its performance degrades quickly as the number of elements in the array increases


def bubble_sort(arr):
    length = len(arr)

    for ix in range(length):
        for jx in range(0, length-ix-1):
            if arr[jx] > arr[jx+1]:
                arr[jx], arr[jx+1] = arr[jx+1], arr[jx]


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print("Sorted array is:", arr)
