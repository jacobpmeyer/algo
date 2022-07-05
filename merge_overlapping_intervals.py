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





a = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
