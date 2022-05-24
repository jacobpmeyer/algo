def twoNumberSum(array, targetSum):
	dct = {}
	output = []
	for num in array:
		matchNum = targetSum - num
		if num in dct:
			output.extend([num, matchNum])
		else:
			dct[matchNum] = num
	return output
