def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J)
        i = 0
        for items in S:
            if items in J:
                i = i + 1
        return i
                
