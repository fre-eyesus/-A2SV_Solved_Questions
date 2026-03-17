class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        rabbits = 0

        for x, freq in count.items():
            group_size = x + 1
            groups = ( freq + x) // group_size
        
            rabbits += groups * group_size

        return rabbits