# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def back(node, curr, sum):
            if not node:
                return
            curr.append(node.val)
            sum += node.val
            if not node.left and not node.right:
                if sum == targetSum:
                    res.append(curr[:])
            else:
                back(node.left,curr,sum)
                back(node.right,curr,sum)
            curr.pop()
        back(root,[],0)
        return res
        