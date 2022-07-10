"""
You are given an integer array arr. From some starting index,
you can make a series of jumps.
The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps,
and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps.
Note that the jumps are numbered, not the indices.

We are moving forward only.
i = 0 = First jump aka. 1, which is odd
i = 1 = Second jump aka. 2, which is even

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j
such that arr[i] <= arr[j] and arr[j] is the smallest possible value.
If there are multiple such indices j, you can only jump to the smallest such index j.

During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j
such that arr[i] >= arr[j] and arr[j] is the largest possible value.
If there are multiple such indices j, you can only jump to the smallest such index j.

It may be the case that for some index i, there are no legal jumps.

A starting index is good if, starting from that index, you can reach the end
of the array (index arr.length - 1) by jumping some number of times
(possibly 0 or more than once).

Return the number of good starting indices.

My strategy is to start from the end of the array and build up a log of
jumps as I go, that way if I hit a point I've already visited, I just return
whatever the running total is + the steps of the jump I am on

-1 for when I can't get to the end of the array

input array = [10,13,12,14,15]
jumps = {
    number at index: [odd jumps to end, even jumps to end]
    15 = [0, 0],
    14 = [1, -1]
    etc.
}

"""
class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        jumpLog = { i: [None, None] for i, _ in enumerate(arr) }
        jumpLog[len(arr) - 1][0], jumpLog[len(arr) - 1][1] = 0, 0

        for pos in reversed(range(len(arr) - 1)):
            self.doOddJump(arr, pos, jumpLog, 1)

        goodJumps = 0
        for i in range(len(arr)):
            if jumpLog[i][0] != -1:
                goodJumps += 1

        return goodJumps


    def doOddJump(self, arr, startingPos, jumpLog, currentJumpCount) -> int:
        nextPos, smallestValue = -1, float("inf")
        for i in range(startingPos + 1, len(arr)):
            if arr[startingPos] <= arr[i] and arr[i] < smallestValue:
                nextPos, smallestValue = i, arr[i]
                break

        if nextPos == -1 or jumpLog[nextPos][1] == -1:
            jumpLog[startingPos][0] = -1
        elif jumpLog[nextPos][1] is not None:
            jumpLog[startingPos][0] = currentJumpCount + jumpLog[nextPos][1]
        else:
            self.doEvenJump(arr, nextPos, jumpLog, currentJumpCount + 1)
            if jumpLog[nextPos][1] == -1:
                jumpLog[startingPos][0] = -1
            else:
                jumpLog[startingPos][0] = currentJumpCount + jumpLog[nextPos][1]


    def doEvenJump(self, arr, startingPos, jumpLog, currentJumpCount) -> int:
        nextPos, largestValue = -1, float("-inf")
        for i in range(startingPos + 1, len(arr)):
            if arr[startingPos] >= arr[i] and arr[i] > largestValue:
                nextPos, largestValue = i, arr[i]


        if nextPos == -1 or jumpLog[nextPos][0] == -1:
            jumpLog[startingPos][1] = -1
        elif jumpLog[nextPos][0] is not None:
            jumpLog[startingPos][1] = currentJumpCount + jumpLog[nextPos][0]
        else:
            self.doOddJump(arr, nextPos, jumpLog, currentJumpCount + 1)
            if jumpLog[nextPos][0] == -1:
                jumpLog[startingPos][1] = -1
            else:
                jumpLog[startingPos][1] = currentJumpCount + jumpLog[nextPos][0]



arr1 = [10,13,12,14,15] #=> 2
arr2 = [2,3,1,1,4] #=> 3
s = Solution()
res1 = s.oddEvenJumps(arr1)
res2 = s.oddEvenJumps(arr2)
print(res1)
print(res2)
