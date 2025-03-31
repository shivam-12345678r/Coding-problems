# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def dfs(node,max_val):
            if  node is None:
                return 0
            cnt = 0
            if node.val >= max_val:
                cnt += 1
            max_val = max(max_val,node.val)
            cnt += dfs(node.left,max_val)
            cnt += dfs(node.right,max_val)
            return cnt
        return dfs(root,root.val)



       
        