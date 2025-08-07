# BruteForce of selection Sort
def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are bigger than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            # Shifting, Not Swapping
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key

inputArr = [8, 5, 3, 9, 1]
insertion_sort(inputArr)
print(inputArr)
# Output: [1, 3, 5, 8, 9]
