class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def help(node,d):
            if not node: return d
            return max(help(node.left,d+1),help(node.right,d+1))
        return help(root,0)
    
class Solution:
    def help(self,node,d):
        if not node: return d
        return max(self.help(node.left,d+1),self.help(node.right,d+1))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.help(root,0)