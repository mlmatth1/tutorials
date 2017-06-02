arr = [1, 10, 20, 47, 59, 63, 75, 88, 99]

def binary_search(a, key):
    low = 0
    high = len(a) - 1
    if low > high:
        return -1

    while low <= high:
        mid = low + ((high - low) / 2)
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

print binary_search(arr, 47)
