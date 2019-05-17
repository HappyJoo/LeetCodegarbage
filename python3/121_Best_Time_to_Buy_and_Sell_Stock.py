class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [7,1,5,3,6,4]  return maximum profit
        # Solution 1
        # boundary conditions
        if not prices:  
            return 0
        
        # or set small to float('inf'), infinity. no need for boundary conditions then.
        small, big = prices[0], 0  
        
        for i in prices:
            # the smallest number
            if small > i:  
                small = i
            # the biggest number after small.
            elif i - small > big:  
                big = i - small
                
        return big


        # Solution 2. 
        min_p, max_p = float('inf'), 0
        for i in range(len(prices)):
            # get the smallest number
            min_p = min(min_p, prices[i])
            # get the biggest profit
            max_p = max(max_p, prices[i] - min_p)
        return max_p