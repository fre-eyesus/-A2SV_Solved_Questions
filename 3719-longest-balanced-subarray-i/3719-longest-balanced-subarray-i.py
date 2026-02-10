class Solution:
    def longestBalanced(self, nums: List[int]) -> int:

            even_number = []
            odd_number = []

            for i in nums:
                if i % 2 == 0:
                    even_number.append(i)
                elif i == 1:
                    continue
                else:
                    odd_number.append(i)
            if len(set(even_number)) == len(set(odd_number)):
                return len(even_number) + len(odd_number)
            else:
                return 0


        