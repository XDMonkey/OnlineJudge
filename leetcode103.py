
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res=[]
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.recursion(root,0)
        for i in range(0,len(self.res)):
            if i%2==1:
                self.res[i].reverse()
        return self.res
    def recursion(self,root,i):
        if root!=None:
            if len(self.res)<i+1:
                self.res.append([])
            self.res[i].append(root.val)
            self.recursion(root.left,i+1)
            self.recursion(root.right,i+1)