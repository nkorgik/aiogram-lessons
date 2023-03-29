def counting_sort(arr):
    """This function is for positive only"""
    max_value = max(arr)
    print(max_value)
    
    count = [0] * (max_value + 1)
    
    for x in arr:
        count[x] += 1
    
    sorted_arr = []
    for i in range(max_value + 1):
        sorted_arr.extend([i] * count[i])
        
    return sorted_arr


if __name__ == "__main__":
    arr = [3, 2, 1, 99, 37]
    result = counting_sort(arr)
    print(result)

    