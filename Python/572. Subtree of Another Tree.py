class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False
        if not subRoot:
            return True

        if root.val == subRoot.val:
            if self.check_same(root, subRoot):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def check_same(self,p,q):
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        return self.check_same(p.left,q.left) and self.check_same(p.right, q.right)