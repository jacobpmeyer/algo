def nonConstructibleChange(coins):
    if len(coins) == 0:
        return 1

    coins.sort()
    total = 0
    for coin in coins:
        if coin > total + 1:
            return total + 1
        else:
            total += coin

    return total + 1
