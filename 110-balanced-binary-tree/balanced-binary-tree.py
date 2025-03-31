
class Solution(object):
    

    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            if lh == -1 or rh == -1 or abs(lh - rh) > 1:

               return -1
            return max(lh,rh) + 1
        return height(root) != -1

       


       
        