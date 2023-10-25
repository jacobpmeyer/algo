def longestPeak(array):
    longest = 0
    i = 1
    while i < len(array) - 1:
        if array[i - 1] >= array[i] or array[i + 1] >= array[i]:
            i += 1
            continue
        l = i - 2
        r = i + 2

        while l >= 0 and array[l] < array[l + 1]:
            l -=1

        while r < len(array) and array[r] < array[r - 1]:
            r += 1

        if r - l - 1 > longest:
            longest = r - l - 1

        i = r

    return longest
