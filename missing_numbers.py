def missingNumbers(nums):
    foundNums = [False for i in range(len(nums) + 2)]
    for num in nums:
        foundNums[num - 1] = True
    missing = []
    for i in range(len(foundNums)):
        if foundNums[i] is False:
            missing.append(i + 1)
    return missing
