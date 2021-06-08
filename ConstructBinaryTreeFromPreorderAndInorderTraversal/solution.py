# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        binaryTree = TreeNode(preorder[0])
        currentRootIndex = inorder.index(binaryTree.val)
        leftSubTree = inorder[:currentRootIndex]
        rightSubTree = inorder[currentRootIndex + 1:]
        binaryTree.left = self.buildTree(preorder[1:currentRootIndex + 1], leftSubTree)
        binaryTree.right = self.buildTree(preorder[currentRootIndex + 1:], rightSubTree)
        return binaryTree
