def maxNum(array):
    max = array[0]
    for num in array:
        if num > max:
            max = num

    return max

def minNum(array):
    min = array[0]
    for num in array:
        if num < min:
            min = num

    return min


