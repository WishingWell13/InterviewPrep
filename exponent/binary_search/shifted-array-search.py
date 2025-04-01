'''
https://www.tryexponent.com/practice/prepare/shifted-array-search


Input: Array once shifted, will be a orted array of integers (distinct) AND number to find

Maybe: Shifted array that is sorted

Output: Index of the number in the original array
                    |       | 
input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left

output: 3 # since it’s the index of 2 in arr

'''


from typing import List

def shifted_arr_search(shiftArr: List[int], num: int) -> int:
    if len(shiftArr) == 0:
        return -1

    # Finding the pivot point
    s = 1
    e = len(shiftArr) - 2

    splitIndex = -1

    if shiftArr[0] == num:
        return 0
    elif shiftArr[-1] == num:
        return len(shiftArr) - 1

    while s < e:
        mid = int((s + e) / 2)

        if shiftArr[mid] == num:
            return mid
        
        # Found case
        elif shiftArr[mid] < shiftArr[mid+1] and shiftArr[mid] < shiftArr[mid-1]:
            splitIndex = mid
            break
        # Check to the right
        elif shiftArr[mid] > shiftArr[-1]:
            s = mid+1
        # Check to left
        else:
            e = mid-1

    # Finding the actual index

    # Select which half to solve
    if num <= end:
        s = splitIndex
        e = len(shiftArr) - 1
    else:
        s = 0
        e = splitIndex - 1

    # Guarenteed that this range is sorted
    while s <= e:
        mid = int((s + e) / 2)

        if shiftArr[mid] == num:
            return mid
        # Check to the right
        elif shiftArr[mid] < num:
            s = mid+1
        # Check to left
        else:
            e = mid-1

    return -1
