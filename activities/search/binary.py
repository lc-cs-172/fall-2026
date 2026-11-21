def _search(haystack, needle, lo : int, hi : int) -> int:
    """Search for needle in haystack between lo (inclusive) and hi (exclusive)."""
    if hi <= lo:
        return -1
    mid = (lo + hi) // 2
    if haystack[mid] < needle:
        return _search(haystack, needle, mid + 1, hi)
    elif needle < haystack[mid]:
        return _search(haystack, needle, 0, mid)
    else:
        return mid

def search(haystack, needle) -> int:
    """Search for needle in sorted haystack, if found return the index else
    -1."""
    n = len(haystack)
    return _search(haystack, needle, 0, n)
