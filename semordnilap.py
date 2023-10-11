def semordnilap(words):
    rev = []
    revMap = {}
    for word in words:
        if word[::-1] in revMap:
            rev.append([word[::-1], word])
        else:
            revMap[word] = True

    return rev
