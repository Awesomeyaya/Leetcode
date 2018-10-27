def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxcur = 0 
        maxprofit = 0 
        for n in range(1,len(prices)):
            maxcur = max(0,prices[n] - prices[n-1] + maxcur)
            maxprofit = max(maxcur,maxprofit)
        return maxprofit
