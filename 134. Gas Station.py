“”“
1.保证有解的条件是 sum(gas) >= sum(cost) 
2. 设置start = 0 : 从第一个位置开始，计算balance = balance + gas-cost 用于判断能不能走到下一个station
  如果不能的话，就从第二个位置开始 start = i + 1 

为什么diff的解法不对？ 

因为不能用总的状态来算，比如3-4+3，表面上看着可以到下一个，其实3 < 4就已经说明，到不了下一站了。
”“”
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        """
        简化一下，求出到达每个station的tank volume
        station     curCost 
        0           gas[-1] - cost[-1] + gas[0] = 5 -2+1 =  4 
        1           gas[0] - cost[0] + gas[1] = 1 - 3 + 2 = -1 
        2           gas[1] - cost[1] + gas[2] = 2-4+3 = -1 
        3           gas[2] - cost[2] + gas[3] = 3 - 5 + 4 = 2 
        4           gas[3] - cost[3] + gas[4] = 4 - 1 + 5 = 8
        
        或者求到下一个station后的tank volume
        0 1-3+2 = 0  -2
        1 2-4+3 = 1  -2
        2 3-5+4 = 2  -2
        3 4-1+5 = 8  3
        4 5-2+1 = 4  3 
        
        
        如果从5号station出发：
        station: 5 tank:5 
        to s1: t = 5 - 2 + 1 = 4 
        to s2: t = 4 - 3 + 2 = 3 
        to s3: t = 3 - 4 < 0 我已经到不了3了
        """
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas) 
        balance = 0 
        start = 0 
        for i in range(n):
            balance += gas[i] - cost[i] 
            if balance < 0:
                balance = 0 
                start = i+1
        return start 
