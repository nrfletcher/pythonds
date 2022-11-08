import time


# Algorithm 1
# Time complexity is O(n)
def sum_of_n(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i

    end = time.time()
    return the_sum, end-start


# Summation formula
# Time complexity is still O(n) but it will have a shorter runtime execution
def sum_of_n_fast(n):
    return (n(n+1))/2


# Naive anagram solver
# Time complexity is O(n^2)
def naive_anagram(s1, s2):
    still_ok = True
    if len(s1) != len(s2):
        return False

    alist = list(s2)
    pos1 = 0

    while pos1 < len(s1) and still_ok:
        # Start at index 0 of our 2nd string each time
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        # If we found it replace it in our 2nd string with none so our quantity of char values is accurate
        if found:
            alist[pos2] = None
        else:
            still_ok = False

        pos1 = pos1 + 1

    return still_ok


# Sorted anagram comparison
# Time complexity is O(nlogn) using the Python sort() function, however this implementation is not consistent
def sorted_anagram(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


# Efficient anagram solver
# Takes advantage of us knowing that anagrams will contain the same number of each unique character
# This runtime complexity is O(n)
def efficient_anagram(s1, s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False

    return still_ok
