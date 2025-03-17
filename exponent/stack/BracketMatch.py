'''
https://www.tryexponent.com/practice/prepare/bracket-match
'''

from collections import deque

def bracket_match(text: str) -> int:
    myMap = {'{': '}', '[': ']', '(': ')'}

    myStack = deque()

    toAdd = 0

    for char in text:

        if char in myMap.keys(): # If opening bracket
            myStack.append(char)
        elif char in myMap.values(): # If closing bracket
            # Too many closing brackets
            if len(myStack) == 0:
                toAdd += 1
                continue
            
            nextElem = myStack.pop()

            if not myMap[nextElem] == char:
                toAdd += 1
        else:
            print("Something went wrong")
    
    return toAdd + len(myStack)
