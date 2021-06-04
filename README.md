# Python Algorithms
## Linear Search
### Code

```python
def search(array, element):
    for x in range(len(array)):
        if array[x] == element:
            return x
    return -1
```

### Test cases

```python
Test_Case_1 = search(['a', 'b', 'c', 'd'], 'b') # 1
Test_Case_2 = search([1, 2, 3, 4, 5, 6], 4) # 3
```

## Binary and Decimal Numbers
### Code

```python
def binaryToDecimal(binary: str):
    return int(binary,2)
    
def decimalToBinary(n):
    return bin(n).replace("0b", "")
```

### Test cases
```python
Test_Case_1 = binaryToDecimal('111') # 7
Test_Case_2 = binaryToDecimal('10111') # 23
Test_Case_3 = decimalToBinary(100) # 1100100
Test_Case_4 = decimalToBinary(69) # 1000101
```
