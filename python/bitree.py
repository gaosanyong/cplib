"""
NAME 
    bitree - binary tree algorithms

DESCRIPTION
    This module implements a few tree-related algorithms. 

    * bfs         breadth-first search
    -----------------------------------------
    * preorder    iterative dfs in  pre-order 
    * inorder     iterative dfs in   in-order 
    * postorder   iterative dfs in post-order 

FUNCTIONS
    bfs(root)
        Return nodes of a binary tree in level-order.

    preorder(root)
        Return nodes of a binary tree in pre-order.

    inorder(root)
        Return nodes of a binary tree in in-order.

    postorder(root)
        Return nodes of a binary tree in post-order.
"""

from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def bfs(root):
    """Return nodes of a binary tree in level-order."""
    ans = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            ans.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return ans 


def dfs(root):
    """Recursively depth-first traverse a binary tree."""
    #   inorder traversal : left-node-right
    #  preorder traversal : node-left-right
    # postorder traversal : left-right-node
    if root: 
        yield from dfs(root.left)
        yield root.val
        yield from dfs(root.right)


def preorder(root):
    """Return nodes of a binary tree in pre-order."""
    ans = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node: 
            ans.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return ans 


def inorder(root):
    """Return nodes of a binary tree in in-order."""
    ans = []
    node = root 
    stack = []
    while node or stack:
        if node: 
            stack.append(node)
            node = node.left 
        else: 
            node = stack.pop() 
            ans.append(node)
            node = node.right 
    return ans 


def postorder(root):
    """Return nodes of a binary tree in post-order."""
    ans = []
    node, prev = root, None
    stack = []
    while node or stack:
        if node: 
            stack.append(node)
            node = node.left 
        else: 
            node = stack[-1] 
            if node.right and node.right != prev: node = node.right 
            else: 
                ans.append(node) 
                stack.pop() 
                prev = node 
                node = None
    return ans 