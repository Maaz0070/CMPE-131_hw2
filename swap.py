def swap_list(arr):
    temp = arr[int((len(arr)-1)/2)]
    arr[int((len(arr)-1)/2)] = arr[len(arr)-1]
    arr[len(arr)-1] = temp
    