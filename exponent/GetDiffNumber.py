'''
https://www.tryexponent.com/practice/prepare/getting-a-different-number
'''

from typing import List

def get_different_number(arr: List[int]) -> int:
    mySet = set()

    for i in arr:
        mySet.add(i)

    if 0 not in mySet:
        return 0

    for i in range(0, len(arr)):
        if i not in mySet:
            return i
    
    return len(arr)
     # your code goes here
