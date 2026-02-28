class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            count = Counter()
            l = 0
            total = 0

            for r in range(len(nums)):
                count[nums[r]] += 1

                while len(count) > k:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1

                total += r - l + 1

            return total

        return atMost(k) - atMost(k - 1)