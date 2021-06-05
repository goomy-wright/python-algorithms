def binary_search(array, element):
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


Test_Case_1 = binary_search([1,4,8,6,9], 8) # 2
Test_Case_2 = binary_search([1,4,8,6,9], 4) # 1