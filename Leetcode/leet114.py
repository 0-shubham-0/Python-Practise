class Solution:
    def preorderTraversal_without_stack(self, root: Optional[TreeNode]) -> List[int]:
            ret = []
            def sol(root):
                if not root:
                    return
                ret.append(root.val)
                sol(root.left)
                sol(root.right)
            sol(root)
            return ret
    def preorderTraversal_with_stack(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack=[root]
        while stack:
            cur=stack.pop()
            if cur:
                ret.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        return ret