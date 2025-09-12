class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        l_max_list = [0] * n
        r_max_list = [0] * n

        max_l = 0
        for i in range(n):
            max_l = max(max_l, height[i])
            l_max_list[i] = max_l

        max_r = 0
        for i in range(n-1, -1, -1):
            max_r = max(max_r, height[i])
            r_max_list[i] = max_r

        ans = 0
        for i in range(n):
            ans += min(r_max_list[i],l_max_list[i]) - height[i]

        return ans  
