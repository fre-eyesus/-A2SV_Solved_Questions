class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        ans = []
        for freq in num_freq:
            ans.append([num_freq[freq],freq])
            ans.sort(reverse=True)
        
        returned = []
        for i in range(k):
            returned.append(ans[i][1])
        return returned 

    