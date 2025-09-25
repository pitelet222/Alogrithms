def binary_search(arr, item):
    arr.sort()
    shortest = 0
    largest = len(arr) - 1
    while shortest <= largest:
        mid = (shortest + largest) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            largest = mid - 1
        else:
            shortest = mid + 1
    return None


result = binary_search([1,43,54,5,43,52,354,45,43,65,464,5,34565,34,53,6,345,53,5,356,34], 52)
print(result)