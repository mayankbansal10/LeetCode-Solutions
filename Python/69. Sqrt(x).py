class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left, right, ans = 0, x, 0

        while left <= right:
            mid = (right + left)//2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                ans = mid 
                left = mid + 1
            else:
                right = mid - 1
                
        return ans
