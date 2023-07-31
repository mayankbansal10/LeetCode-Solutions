class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            self.max_path_sum = max(
                self.max_path_sum, left_sum + node.val + right_sum)
            return node.val + max(left_sum, right_sum)

        self.max_path_sum = float(-inf)

        dfs(root)

        return self.max_path_sum
