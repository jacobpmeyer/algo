def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    total = 0
    if fastest:
        blueShirtSpeeds.sort(reverse = True)
    else:
        blueShirtSpeeds.sort()

    for i in range(len(blueShirtSpeeds)):
        total += max(blueShirtSpeeds[i], redShirtSpeeds[i])

    return total

"""
reds:
[2, 3, 5, 5, 9]

blues:
minimum:
[1, 2, 3, 6, 7]
fastest:
[7, 6, 3, 2, 1]


pairs = len(speeds)
[9, 1][7, 2][6, 3][5, 3][5, 2]
9 7 6 5 5
"""
