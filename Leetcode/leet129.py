class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def help(head,n):
            if not head:
                return 0
            n=(n*10)+head.val
            if not head.left and not head.right:
                return n
            l=help(head.left,n)
            r=help(head.right,n)
            return r+l
        return help(root,0)
