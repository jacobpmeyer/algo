def commonCharacters(strings):
    commons = {}
    output = []

    for i, string in enumerate(strings):
        for char in string:
            if i == 0:
                commons[char] = 1
            elif char in commons:
                if commons[char] == i:
                    commons[char] += 1

    for key, value in commons.items():
        if value == len(strings):
            output.append(key)

    return output
