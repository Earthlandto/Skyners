def checkio(data):

    data.sort()
    length = len(data)
    out = data[length/2]

    # if length is even, add the other central term, else, out has already the result
    if length % 2 == 0 :
        out = (out + data[length/2-1]) / float(2)

    return out
