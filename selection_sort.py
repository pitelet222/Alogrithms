def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    
def selection_sort(arr):
    newArr = []
    copied_arr = list(arr)
    for i in range(len(copied_arr)):
        smallest = find_smallest(copied_arr)
        newArr.append(copied_arr.pop(smallest))
    return newArr

result = selection_sort([112,4,54,45,5464,56,345,4,345,6,45,45,66,6,54,543,6,345,6,6,45,435]) 
print(result)  
    