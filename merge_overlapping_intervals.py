"""
sort array
iterate over array
if current start <= previous end
previous end = current end
else current pair, appended to return array
"""
def mergeOverlappingIntervals(intervals):
  intervals.sort()
  condensedIntervals = [intervals[0]]
  for i in range(1, len(intervals)):
    currentPair = intervals[i]
    lastCondensed = condensedIntervals[-1]
    if currentPair[0] <= lastCondensed[1] and lastCondensed[1] <= currentPair[1]:
      lastCondensed[1] = currentPair[1]
    if currentPair[0] <= lastCondensed[1]:
      continue
    else:
      condensedIntervals.append(currentPair)
  return condensedIntervals


"""
This solution passes.
If you know your max value is going to be less than the length of the input array,
this would be better, if not, the above is still better.
"""
def mergeOverlappingIntervals(intervals):
    intDict = {}
    maxInt = float('-inf')
    minInt = float('inf')
    for i in intervals:
        intDict[i[0]] = i[1]
        if i[0] > maxInt:
            maxInt = i[0]
        if i[0] < minInt:
            minInt = i[0]
    i = minInt
    while i <= maxInt:
        if i not in intDict:
            i += 1
            continue
        nextMax = intDict[i]
        j = i + 1
        while j <= nextMax:
            if j in intDict:
                if nextMax <= intDict[j]:
                    intDict[i] = intDict[j]
                    nextMax = intDict[j]
                del intDict[j]
            j += 1
        i += 1
    output = []
    for key, value in intDict.items():
        output.append([key, value])
    return output



a = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
