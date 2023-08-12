class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.count=0
        n=len(coins)
        def sol(curr_sum,i):
            if curr_sum>amount or i>n-1:
                return
            if curr_sum==amount:
                self.count+=1
                return
            sol(curr_sum+coins[i],i)
            sol(curr_sum,i+1)
        sol(0,0)
        return count
    
