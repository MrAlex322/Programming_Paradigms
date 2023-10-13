def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1  

sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_element = 11

result = binary_search(sorted_array, target_element)
if result != -1:
    print(f"Элемент {target_element} найден по индексу {result}.")
else:
    print(f"Элемент {target_element} не найден в массиве.")
