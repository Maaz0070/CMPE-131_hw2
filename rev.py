def reverse_list(arr):
    for i in range(0, len(arr)-1):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
        return arr
        