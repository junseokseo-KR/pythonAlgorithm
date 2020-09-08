def binary_search(element, some_list):
    startIdx = 0
    endIdx = int(len(some_list)-1)

    while startIdx<=endIdx:
        midIdx = int((endIdx+startIdx)/2)
        midVal = some_list[midIdx]

        if element == midVal:
            return midIdx
        elif element < midVal:
            endIdx = midIdx-1
        else: #element > midVal
            startIdx = midIdx+1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))