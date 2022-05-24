def isValidSubsequence(array, sequence):
	if len(sequence) > len(array):
		return False
	j = 0
	for i, num in enumerate(array):
		if j == len(sequence):
			break
		if num == sequence[j]:
			j += 1
	return j == len(sequence)
