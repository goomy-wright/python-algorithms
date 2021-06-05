## Binary Numbers

```python
def binaryToDecimal(binary: str):
    return int(binary,2)

def decimalToBinary(n):
    return bin(n).replace("0b", "")

Test_Case_1 = binaryToDecimal('111') # 7
Test_Case_2 = decimalToBinary(100) # 1100100
```

## Binary Search

```python
def binarySearch(array, element):
    start = 0
    end = len(array) - 1

    while(start <= end):
        mid = (start + end) // 2
        if(array[mid] > element):
            end = mid - 1
        elif(array[mid] < element):
            start = mid + 1
        else:
            return mid
    
    return None

Test_Case_1 = binarySearch([1,4,8,6,9], 8) # 2
Test_Case_2 = binarySearch([1,4,8,6,9], 4) # 1
```