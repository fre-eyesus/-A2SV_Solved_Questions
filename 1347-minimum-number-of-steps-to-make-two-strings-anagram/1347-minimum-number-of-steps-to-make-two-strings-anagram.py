class Solution:
    def minSteps(self, s: str, t: str) -> int:
        min_steps = 0
        count_s= Counter(s)
        count_t = Counter(t)


        se = set(s)
        if count_s == count_t:
            return 0

        for i in se:
            if count_s.get(i,0) > count_t.get(i,0):
                min_steps += abs(count_s.get(i,0) - count_t.get(i,0))
       
        return min_steps
        
            