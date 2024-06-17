def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
arr = [133, 99, 11, 5,23]
sorted_arr = insertion_sort(arr)
print("Insertion Sort:", sorted_arr)
