"""
Question 1) How would you find the number equal or of if the equal not found, closest number that is less in a sorted array.
"""


def find_closest(lst, n):
    """
    :type l: list
    :type n: int
    :rtype: int
    Finds the largest number equal to or less than a provided number in a sorted list
    """
    # I don't trust that this array is sorted... also guarantees sorted in ascending order
    nums = sorted(lst)  # Optional, don't care about time complexity
    
    # this is more or less binary search, except instead of returning the index we return the number itself
    def _search(sl, t):
        if len(sl) == 1:
            return sl[0]
        if len(sl) == 2:
            if sl[1] <= t:
                return sl[1]
            else:
                return sl[0]
        mid = sl[len(sl)//2]
        if t == mid:
            return mid
        elif t < mid:
            # Search the first half of sl
            return _search(sl[:len(sl)//2], t)
        else:
            # Search the second half of sl
            return _search(sl[len(sl)//2:], t)
    # import ipdb; ipdb.set_trace()
    return _search(nums, n)

