def bestSeat(seats):
    if len(seats) <= 2:
        return -1

    right = 0
    while right < len(seats) and seats[right] == 1:
            right += 1

    right -= 1
    left = right
    bestGap = 0
    bestSeat = -1


    while left < len(seats) - 1 and right < len(seats):
        left = right + 1
        while seats[left] == 0:
            left += 1

        if left - right > bestGap:
            bestGap = left - right
            bestSeat = (left + right) // 2
        right = left

    return bestSeat
