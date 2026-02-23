class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count_s = Counter(s)

        remain = list(set(s)-set(order))

        ans = ''
        for o in order:
            if o in count_s:
                ans+= o*(count_s[o])
        re = ''
        for r in remain:
            re+= r*(count_s[r])
        return ans + re