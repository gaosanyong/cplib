"""
NAME 
    tree - tree algorithms

DESCRIPTION
    This module implements a few tree-related algorithms. 

    * dfs_preorder   - iterative preorder depth-first search
    * dfs_inorder    - iterative inorder depth-first search
    * dfs_postorder  - iterative postorder depth-first search
    * bfs            - breadth-first search

FUNCTIONS
    dfs_preorder(root)
        Traverse a binary tree depth-first in preorder.

    dfs_inorder(root)
        Traverse a binary tree depth-first in inorder.

    dfs_postorder(root)
        Traverse a binary tree dpeth-first in postorder.

    bfs(root)
        Traverse a binary tree breadth-first.
"""

def dfs_preorder(root):
    """Traverse a binary tree depth-first in preorder."""
    ans = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            ans.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return ans 


def dfs_inorder(root):
    """Traverse a binary tree dpeth-first in inorder."""
    ans = []
    node, stack = root, []
    while node or stack:
        if node:
            stack.append(node)
            node = node.left 
        else: 
            node = stack.pop()
            ans.append(node.val)
            node = node.right
    return ans 


def dfs_postorder(root):
    """Traverse a binary tree depth-first in postorder."""
    ans = []
    node, stack = root, []
    prev = None 
    while node or stack:
        if node: 
            stack.append(node)
            node = node.left 
        else: 
            node = stack[-1] 
            if node.right and node.right != prev: node = node.right 
            else: 
                ans.append(node.val) 
                stack.pop() 
                prev = node 
                node = None
    return ans 


def bfs(root):
    """Traverse a binary tree breadth-first."""
    ans = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            ans.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return ans 