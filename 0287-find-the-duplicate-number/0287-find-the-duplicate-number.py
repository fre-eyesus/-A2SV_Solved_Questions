class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
            # ans = -1

            count = Counter(nums).most_common()
            return count[0][0]
            
          