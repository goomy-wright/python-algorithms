## Duplicate Numbers

```python
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


Test_Case_1 = findDuplicate([1,5,7,3,1]) # 1
Test_Case_2 = findDuplicateNumbers([1,7,3,1,7,8,9]) # [1, 7]
```

## Linear Search

```python
def search(array, element):
    for x in range(len(array)):
        if array[x] == element:
            return x
    return -1

Test_Case_1 = search(['a', 'b', 'c', 'd'], 'b') # 1
Test_Case_2 = search([1, 2, 3, 4, 5, 6], 4) # 3
```

## Min and Max Numbers

```python
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

Test_Case_1 = maxNum([1,2,3,4,5,8]) # 8
Test_Case_2 = minNum([5,8,3,9,10]) # 3
```