class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def ist(p, q):
            if p == None and q == None:
                return True
            if p == None or q == None:
                return False
            return p.val == q.val and ist(p.left, q.left) and ist(p.right, q.right)

        return ist(p, q)
