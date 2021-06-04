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
#### Binary numbers to Decimal

```python
def binaryToDecimal(binary: str):
    return int(binary,2)
```

### Decimal numbers to Binary
```python
def decimalToBinary(n):
    return bin(n).replace("0b", "")
```
