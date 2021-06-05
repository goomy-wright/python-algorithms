def findDuplicate(array):
    array.sort()
    for x in range(1, len(array)):
        if array[x] == array[x - 1]:
            return array[x]

    return None

def findDuplicateNumbers(array):
    n = []
    array.sort()

    for i in range(1, len(array)):
        if array[i] == array[i-1]:
            n.append(array[i])

    return n

