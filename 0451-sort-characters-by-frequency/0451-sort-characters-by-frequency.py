class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        common = count.most_common()
        count_sorted = dict(common)
        ans = ""
        for key, value in count_sorted.items():
            ans+= key*value
        return ans

        