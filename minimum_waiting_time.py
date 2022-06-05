# the input array contains positive integers representing the amounts of time
# that specific queries take to execute
#
# Only one query can be executed at a time but the queries can be executed in
# any order
#
# The waiting time of a query is the sum of the time the queries before it took
# to run.
#
# Sample input: [3, 2, 1, 2, 6]
# Sample output: 17

# [3, 2, 1, 5, 6, 4]
# [0, 3, 5, 6, 11, 17]

# [1, 2, 3, 4, 5, 6]
# [0, 1, 3, 6, 10, 15]

# sort the queries array, then generate another array of times
# add previous cumulative time to previous query time until you get to the
# end of the array
# The waiting times array should be the same length as the queries array
# return sum of waiting times
def minimumWaitingTime(queries):
    waitingTimes = [0 for i in range(len(queries))]
    queries.sort()

    for i in range(1, len(queries)):
        waitingTimes[i] = waitingTimes[i - 1] + queries[i - 1]

    return sum(waitingTimes)
