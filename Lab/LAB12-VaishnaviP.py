def maxLen(arr):
    Longestsubarray = 0
    total = 0
    SumIdx = {}

    for i, val in enumerate(arr):
        total += val

        if total == 0:
            Longestsubarray = i + 1

        if total in SumIdx:
            Longestsubarray = max(Longestsubarray, i - SumIdx[total])
        else:
            SumIdx[total] = i

    return Longestsubarray


print(maxLen([1, 2, 3, 4, 5]))
print(maxLen([15, -2, 2, -8, 1, 7, 10, 13]))
