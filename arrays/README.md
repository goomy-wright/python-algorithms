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