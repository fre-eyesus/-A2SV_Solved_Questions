class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:      
        ans = []
        even_sum = sum(x for x in nums if x % 2 == 0)  # initial sum of evens

        for q in queries:
            val = q[0]
            index = q[1]

            
            if nums[index] % 2 == 0:
                even_sum -= nums[index]


            nums[index] += val


            if nums[index] % 2 == 0:
                even_sum += nums[index]

            ans.append(even_sum)

        return ans
