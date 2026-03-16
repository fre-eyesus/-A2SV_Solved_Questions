class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund = []

        half = len(costs) // 2
        cost = 0

        for A, B in costs:
            refund.append(B - A)
            cost += A
        
        refund.sort()
        
        for i in range(half):
            cost += refund[i]
        
        return cost
