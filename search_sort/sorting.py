# There are many different methods of sorting data, some methods better than other depending on the exact goal


# Bubble sort is O(n^2), and objectively a very inefficient algorithm. It's not useful for much else other than to
# show a naive sorting method that is easy to understand. It simply swaps values as it iterates when necessary
def bubble_sort(items):
    for i in range(len(items)-1, 0, 1):
        for j in range(i):
            if items[j] > items[j + 1]:
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp


# A short bubble is taking advantage of the fact that if a complete pass results in no swaps, it's already sorted
# Many sorting algorithms don't do iterative sweeps, so this is a rare advantage a short bubble has
def short_bubble(items):
    swaps = True
    index = len(items) - 1
    while index > 0 and swaps:
        swaps = False
        for i in range(index):
            if items[i] > items[i + 1]:
                swaps = True
                temp = items[i]
                items[i] = items[i + 1]
                items[i + 1] = temp
        index -= 1


# Selection sort, while also O(n^2) is an improvement over bubble sort by acting a bit smarter
# Each iteration we check for the largest value in the range n - 1 and swap it with some number to the end
def selection_sort(items):
    for i in range(len(items)-1, 0, -1):
        index = 0
        for j in range(1, i + 1):
            if items[j] > items[index]:
                index = j

        temp = items[i]
        items[i] = items[index]
        items[index] = temp


# Insertion sort uses a sublist starting with just one value, and adding each new item as we traverse into the sublist
# which is always sorted. Once again, due to having to check each value for each n, this is still O(n^2).
def insertion_sort(items):
    for i in range(1, len(items)):
        curr = items[i]
        index = i
        while index > 0 and items[index - 1] > curr:
            items[index] = items[index - 1]
            index -= 1
        items[index] = curr


# Shell sort is also a different approach but utilizes insertion sort. Shell sort takes a random interval (such as 3)
# and does insertion sort but creates spaced sublists using said interval to increase the overall order of the list
def shell_sort(items):
    def gap_insertion(values, start, gap):
        for i in range(start + gap, len(values), gap):
            curr = values[i]
            pos = i

            while pos >= gap and values[pos - gap] > curr:
                values[pos] = values[pos - gap]
                pos = pos - gap

            values[pos] = curr

    sublists = len(items) // 2

    while sublists > 0:
        for i in range(sublists):
            gap_insertion(items, i, sublists)

        sublists = sublists // 2


# Merge sort is a recursive divide and conquer algorithm that takes advantage of list splitting to split our list up
# This algorithm is O(nlogn) since the larger the list the bigger the splits (logn) and it must do it for every item (n)
def merge_sort(items):
    if len(items) > 1:
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]

        # Calling merge sort on each sublist until we reach a base case of 1 item, which by default is sorted
        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                items[k] = left[i]
                i += 1
            else:
                items[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            items[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            items[k] = right[j]
            j += 1
            k += 1


# Quick sort is an improvement on merge sort as it does not require additional space for sublists, however due to the
# pivot value generation it can sometimes devolve to O(n^2). Average case is O(nlogn) with less space complexity
def quick_sort(items):
    quick_sort_helper(items, 0, len(items) - 1)


def partition(items, first, last):
    pivot = items[first]

    left = first + 1
    right = last

    done = False
    while not done:
        while left <= right and items[left] <= pivot:
            left += 1
        while items[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            temp = items[left]
            items[left] = items[right]
            items[right] = temp

    temp = items[first]
    items[first] = items[right]
    items[right] = temp

    return right


def quick_sort_helper(items, first, last):
    if first < last:
        split = partition(items, first, last)

        quick_sort_helper(items, first, split - 1)
        quick_sort_helper(items, split + 1, last)


l = [4, 5, 6, 2, 6, 7, 3, 7, 3, 4]
quick_sort(l)
print(l)
