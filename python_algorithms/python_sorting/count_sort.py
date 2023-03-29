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


def counting_sort(arr):
    """This if for negative counting sort"""
    shift = abs(min(arr))
    shifted_arr = [x + shift for x in arr]

    max_val = max(shifted_arr)

    count = [0] * (max_val + 1)

    for num in shifted_arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_arr.append(i - shift)

    return sorted_arr



if __name__ == "__main__":
    arr = [3, 2, 1, 99, 37]
    result = counting_sort(arr)
    print('POSITIVE: ', result, sep='\n')

    my_list = [5, -3, 8, -1, 0, -2, 4]
    sorted_list = counting_sort(my_list)
    print('NEGATIVE: ', sorted_list, sep='\n')
    