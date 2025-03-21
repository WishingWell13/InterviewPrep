
'''
https://www.tryexponent.com/practice/prepare/balanced-tree

BFS - Depths

      a
     / \
    b   c
   /   / \
  d   z   e
           \
            g 
             \
              q

Base case: If both our nodes are null, balanced and return our depth

Recursively call each subtree, see if |left depth - right depth| > 1, then unbalanced

'''

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
def find_depth(node, currDepth):
    # Base Case
    if node is None:
        return currDepth-1
    
    # Recursive Case
    getLeft = find_depth(node.left, currDepth+1)
    getRight = find_depth(node.right, currDepth+1)

    if getLeft == -1 or getRight == -1:
        return -1

    if(abs(getLeft - getRight) > 1):
        return -1

    return max(getLeft, getRight)

def is_balanced(node):
    # your code goes here
    if node is None:
        return True

    # Base Case
    if node.left is None and node.right is None:
        return True

    res = find_depth(node, 1)

    return res != -1
    
    
# debug your code below
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print(is_balanced(root)) 
