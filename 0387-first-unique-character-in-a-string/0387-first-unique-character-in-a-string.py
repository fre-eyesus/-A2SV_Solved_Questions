class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        nrp = 0
        for k, v in count.items():
            if v == 1:
                nrp = k
                break
            
        l = list(s)
        if nrp:   
            for i,e in enumerate(l):
                if nrp == e:
                    return i
                    
        else:
            return -1


        