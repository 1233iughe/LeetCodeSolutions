# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive implementation (mine)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Check if root exists
        if root != None:
            
            #Setting pointers to left and right nodes
            l,r = None, None

            #If a child exists then assign it to the opposite pointer (since they are gonna be swapped)
            if root.right:
                l = root.right
            if root.left:
                r = root.left

            #If both exist, swap them, and call the function for both.
            if l and r:
                root.left = l
                root.right = r
                self.invertTree(r)
                self.invertTree(l)
            #If only one exists assign its value to the other, and set it to none and call the function to the existing node.
            elif l:
                root.left = l
                root.right = None
                self.invertTree(l)
            else:
                root.right = r
                root.left = None
                self.invertTree(r)

        return root
#Neetcode implementation
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
