class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
           return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2) - len(s1)):
            if s1_count == s2_count:
                return True
            
            s2_count[ord(s2[i]) - ord('a')] -= 1
            s2_count[ord(s2[i + len(s1)]) - ord('a')] +=1

        return s2_count == s1_count
