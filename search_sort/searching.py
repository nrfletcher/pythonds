# Searching for items in a list

# The most naive searching algorithm possible, iterate from 0 to len(lst) looking for said value
def sequential_search(lst, value):
    for i in lst:
        if i == value:
            return True
    return False


# Assuming a sorted array of values, we can slightly improve by stopping once we either find or exceed the value
def sequential_search_sorted(lst, value):
    i = 0
    while i < len(lst):
        if lst[i] == value:
            return True
        if lst[i] > value:
            return False
    return False


# Binary search once again takes advantage of a sorted array, by first checking the middle value and going from there
# Binary search is O(logn)
def binary_search(lst, value):
    low = 0
    high = len(lst) - 1

    while low <= high:

        # Note that we can also use low + (high - low) // 2 to ensure we do not run into an integer overflow issue
        mid = (low + high) // 2

        if value == lst[mid]:
            return mid
        elif value < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# Recursive binary search  (requires the length of list in arguments)
def recursive_bs(lst, value, low, high):
    if low > high:
        print('Not here')
        return

    mid = low + (high - low) // 2
    print(mid)
    if lst[mid] == value:
        print('Found ' + str(lst[mid]))
    elif value < lst[mid]:
        recursive_bs(lst, value, low, mid - 1)
    else:
        recursive_bs(lst, value, mid + 1, high)


recursive_bs([1, 3, 5, 7, 9, 11, 13, 15, 17, 18, 223], 12, 0, 11)
